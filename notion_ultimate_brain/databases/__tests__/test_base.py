from notion_client import Client

from notion_ultimate_brain.databases.base import UltimateBrainDatabase
from notion_ultimate_brain.notion.all import NotionDatabase


class TestUltimateBrainDatabase:
    def test_create(self):
        raw_data = {"id": "database_id"}
        notion = Client()
        ub_database = UltimateBrainDatabase(notion, raw_data)
        assert isinstance(ub_database, NotionDatabase)
        assert isinstance(ub_database, UltimateBrainDatabase)
        assert ub_database._raw == raw_data
        assert ub_database.id == raw_data["id"]

    def test_default_database_id(self):
        class DummyUBDatabse(UltimateBrainDatabase):
            database_id: str = "static-database-id"

        notion = Client()
        ub_database = DummyUBDatabse(notion)
        assert ub_database._raw == {"id": DummyUBDatabse.database_id}
        assert ub_database.id == DummyUBDatabse.database_id
