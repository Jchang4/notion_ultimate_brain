from unittest.mock import MagicMock

from notion_ultimate_brain.databases.projects import ProjectsDatabase
from notion_ultimate_brain.helpers import get_day_midnight, to_notion_strftime
from notion_ultimate_brain.notion.__tests__.helpers import (
    get_pages_fixture,
    notion_client_fixture,
)
from notion_ultimate_brain.notion.all import NotionPage
from notion_ultimate_brain.pages.project import ProjectPage


class TestProjectsDatabase:
    def test_create(self, notion: MagicMock):
        raw_data = {"id": "database_id"}
        projects = ProjectsDatabase(notion, raw_data)
        assert isinstance(projects, ProjectsDatabase)
        assert projects._raw == raw_data
        assert projects.id == raw_data["id"]

    def test_default_database_id(self, notion: MagicMock):
        projects = ProjectsDatabase(notion)
        assert projects._raw == {"id": ProjectsDatabase.id}
        assert projects.id == ProjectsDatabase.id

    def test_update_id_to_pages(self, notion: MagicMock):
        database = ProjectsDatabase(notion)
        assert not database.id_to_page

        expected_pages = {
            f"page_{i}": NotionPage(database, {"id": f"page_{i}"}) for i in range(5)
        }
        database._update_id_to_pages(list(expected_pages.values()))
        assert database.id_to_page

        assert len(database.id_to_page) == len(expected_pages)

        for page_id, actual_page in database.id_to_page.items():
            assert isinstance(actual_page, ProjectPage)
            assert page_id in expected_pages
            expected_page = expected_pages[page_id]
            assert actual_page._raw == expected_page._raw
            assert actual_page.id == expected_page.id

    def test_today(self, notion: MagicMock, get_pages: MagicMock):
        projects = ProjectsDatabase(notion)

        projects.today

        start = get_day_midnight()
        get_pages.assert_called_once_with(
            query_filter={
                "and": [
                    {
                        "property": "Status",
                        "select": {"equals": "Doing"},
                    },
                    {
                        "or": [
                            {
                                "property": "Completed",
                                "date": {
                                    "is_empty": True,
                                },
                            },
                            {
                                "property": "Completed",
                                "date": {
                                    "after": to_notion_strftime(start),
                                },
                            },
                        ]
                    },
                ]
            }
        )
