from unittest.mock import MagicMock

from notion_ultimate_brain.databases.base import UltimateBrainDatabase
from notion_ultimate_brain.notion.__tests__.helpers import notion_client_fixture
from notion_ultimate_brain.notion.all import NotionDatabase


class TestUltimateBrainDatabase:
    def test_create(self, notion: MagicMock):
        raw_data = {"id": "database_id"}
        ub_database = UltimateBrainDatabase(notion, raw_data)
        assert isinstance(ub_database, NotionDatabase)
        assert isinstance(ub_database, UltimateBrainDatabase)
        assert ub_database._raw == raw_data
        assert ub_database.id == raw_data["id"]

    def test_default_database_id(self, notion: MagicMock):
        class DummyUBDatabase(UltimateBrainDatabase):
            id: str = "static-database-id"

        ub_database = DummyUBDatabase(notion)
        assert ub_database._raw == {"id": DummyUBDatabase.id}
        assert ub_database.id == DummyUBDatabase.id
