from unittest.mock import MagicMock

from notion_ultimate_brain.databases.resources import ResourcesDatabase
from notion_ultimate_brain.notion.__tests__.helpers import (
    TEST_DATABASE_DATA,
    TEST_PAGE_DATA,
    notion_client_fixture,
)
from notion_ultimate_brain.notion.all import NotionPage
from notion_ultimate_brain.pages.resource import ResourcePage


class TestResourcesDatabase:
    def test_base_database_query_filter(self):
        assert ResourcesDatabase.base_database_query_filter == {
            "and": [{"property": "Type", "select": {"equals": "Resource"}}]
        }

    def test_update_id_to_pages(self, notion: MagicMock):
        database = ResourcesDatabase(notion, TEST_DATABASE_DATA)
        assert not database.id_to_page

        expected_pages = {
            f"page_{i}": NotionPage(database, {"id": f"page_{i}"}) for i in range(5)
        }

        database._update_id_to_pages(list(expected_pages.values()))
        assert database.id_to_page

        assert len(database.id_to_page) == len(expected_pages)

        for page_id, actual_page in database.id_to_page.items():
            assert isinstance(actual_page, ResourcePage)
            assert page_id in expected_pages
            expected_page = expected_pages[page_id]
            assert actual_page._raw == expected_page._raw
            assert actual_page.id == expected_page.id
