from unittest.mock import MagicMock

from notion_ultimate_brain.notion.__tests__.helpers import (
    TEST_DATABASE_DATA,
    TEST_PAGE_DATA,
    notion_client_fixture,
)
from notion_ultimate_brain.notion.database import NotionDatabase
from notion_ultimate_brain.notion.page import NotionPage


class TestNotionPage:
    def test_create(self, notion: MagicMock):
        database = NotionDatabase(notion, TEST_DATABASE_DATA)
        page = NotionPage(database, TEST_PAGE_DATA)
        assert page is not None
        assert page.database == database
        assert page.notion == notion
        assert page._raw == TEST_PAGE_DATA
        assert page.id == TEST_PAGE_DATA["id"]
        assert page.title == page.format_title([])
        assert page.parent == TEST_PAGE_DATA["parent"]
        assert page.url == TEST_PAGE_DATA["url"]
        assert page.archived == TEST_PAGE_DATA["archived"]
