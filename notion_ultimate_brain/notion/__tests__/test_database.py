from unittest.mock import MagicMock

from notion_ultimate_brain.notion.__tests__.helpers import (
    TEST_DATABASE_DATA,
    TEST_PAGE_DATA,
    notion_client_fixture,
)
from notion_ultimate_brain.notion.database import NotionDatabase
from notion_ultimate_brain.notion.page import NotionPage


class TestNotionDatabase:
    def test_create(self, notion: MagicMock):
        database = NotionDatabase(notion, TEST_DATABASE_DATA)
        assert database is not None
        assert database.notion == notion
        assert database._raw == TEST_DATABASE_DATA
        assert database.id == TEST_DATABASE_DATA["id"]
        assert database.title == database.format_title(TEST_DATABASE_DATA["title"])
        assert database.parent == TEST_DATABASE_DATA["parent"]
        assert database.url == TEST_DATABASE_DATA["url"]
        assert database.archived == TEST_DATABASE_DATA["archived"]

    def test_update_id_to_pages(self, notion: MagicMock):
        database = NotionDatabase(notion, TEST_DATABASE_DATA)
        assert not database.id_to_page

        page = NotionPage(database, TEST_PAGE_DATA)
        database._update_id_to_pages([page])
        assert database.id_to_page
        assert page.id in database.id_to_page
        assert database.id_to_page[page.id] == page

    def test_pages(self, notion: MagicMock):
        database = NotionDatabase(notion, TEST_DATABASE_DATA)
        assert not database.pages

        page = NotionPage(database, TEST_PAGE_DATA)
        database._update_id_to_pages([page])
        assert database.pages == [page]

    def test_get_pages(self, notion: MagicMock):
        expected_filter = {
            "and": [{"property": "some prop 1", "checkbox": True}],
            "or": [
                {"property": "some prop 1", "date": {"due_on_or_before": "2022-12-12"}}
            ],
        }

        database = NotionDatabase(notion, TEST_DATABASE_DATA)
        database.get_pages(expected_filter)

        notion.databases.query.assert_called_once_with(
            database_id=database.id,
            filter=expected_filter,
        )
