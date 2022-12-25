from unittest.mock import MagicMock

from notion_ultimate_brain.notion.__tests__.helpers import (
    TEST_DATABASE_DATA,
    notion_client_fixture,
)
from notion_ultimate_brain.notion.base import NotionBase


class TestNotionBase:
    def test_create(self, notion: MagicMock):
        base = NotionBase(notion, TEST_DATABASE_DATA)
        assert base.id == TEST_DATABASE_DATA["id"]
        assert base.title == base.format_title(TEST_DATABASE_DATA["title"])
        for key in TEST_DATABASE_DATA["parent"].keys():
            assert base.parent[key] == TEST_DATABASE_DATA["parent"][key]
        assert base.url == TEST_DATABASE_DATA["url"]
        assert base.archived == TEST_DATABASE_DATA["archived"]
