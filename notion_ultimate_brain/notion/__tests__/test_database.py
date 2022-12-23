from notion_client import Client

from notion_ultimate_brain.notion.__tests__.helpers import TEST_DATABASE_DATA
from notion_ultimate_brain.notion.database import NotionDatabase


class TestNotionDatabase:
    def test_create(self):
        notion = Client()
        database = NotionDatabase(notion, TEST_DATABASE_DATA)
        assert database is not None
        assert database.notion == notion
        assert database._raw == TEST_DATABASE_DATA
        assert database.id == TEST_DATABASE_DATA["id"]
        assert database.title == database.format_title(TEST_DATABASE_DATA["title"])
        assert database.parent == TEST_DATABASE_DATA["parent"]
        assert database.url == TEST_DATABASE_DATA["url"]
        assert database.archived == TEST_DATABASE_DATA["archived"]
