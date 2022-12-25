from unittest.mock import MagicMock

from notion_ultimate_brain.databases.all import ProjectsDatabase
from notion_ultimate_brain.notion.__tests__.helpers import (
    TEST_PAGE_DATA, notion_client_fixture)
from notion_ultimate_brain.notion.page import NotionPage
from notion_ultimate_brain.pages.project import ProjectPage


class TestProjectPage:
    def test_create(self, notion: MagicMock):
        page = ProjectPage(ProjectsDatabase(notion), TEST_PAGE_DATA)
        assert isinstance(page, NotionPage)
        assert page._raw == TEST_PAGE_DATA
        assert page.id == TEST_PAGE_DATA["id"]

    def test_base_task_filter(self, notion: MagicMock):
        page = ProjectPage(ProjectsDatabase(notion), TEST_PAGE_DATA)
        assert page.base_task_filter == {
            "property": "Project",
            "relation": {"contains": TEST_PAGE_DATA["id"]},
        }
