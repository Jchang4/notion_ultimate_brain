from unittest.mock import MagicMock

from notion_ultimate_brain.databases.all import ResourcesDatabase
from notion_ultimate_brain.notion.__tests__.helpers import (
    TEST_PAGE_DATA, notion_client_fixture)
from notion_ultimate_brain.notion.page import NotionPage
from notion_ultimate_brain.pages.resource import ResourcePage


class TestResourcePage:
    def test_create(self, notion: MagicMock):
        page = ResourcePage(ResourcesDatabase(notion), TEST_PAGE_DATA)
        assert isinstance(page, NotionPage)
        assert page._raw == TEST_PAGE_DATA
        assert page.id == TEST_PAGE_DATA["id"]
