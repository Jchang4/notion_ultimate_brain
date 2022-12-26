from unittest.mock import MagicMock

from notion_ultimate_brain.databases.all import AreasDatabase, ProjectsDatabase
from notion_ultimate_brain.notion.__tests__.helpers import (
    TEST_PAGE_DATA,
    get_pages_fixture,
    notion_client_fixture,
)
from notion_ultimate_brain.notion.page import NotionPage
from notion_ultimate_brain.pages.area import AreaPage


class TestAreaPage:
    def test_create(self, notion: MagicMock):
        page = AreaPage(AreasDatabase(notion), TEST_PAGE_DATA)
        assert isinstance(page, NotionPage)
        assert page._raw == TEST_PAGE_DATA
        assert page.id == TEST_PAGE_DATA["id"]

    def test_get_projects(self, notion: MagicMock, get_pages: MagicMock):
        page = AreaPage(AreasDatabase(notion), TEST_PAGE_DATA)
        page.get_projects()

        get_pages.assert_called_once_with(
            query_filter={
                "and": [
                    {"property": "Area", "relation": {"contains": page.id}},
                ],
            },
        )
