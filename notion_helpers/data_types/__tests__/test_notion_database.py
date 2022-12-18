from datetime import datetime

from helpers import nonnulls
from notion_helpers.data_types.__tests__.database_data import DATABASE_DATA
from notion_helpers.data_types.notion_database import Database
from notion_helpers.data_types.notion_properties.helpers import get_properties


class TestDatabase:
    raw_database_data = DATABASE_DATA[0]

    def test_create_database_from_raw(self):
        d = Database(self.raw_database_data)
        assert d._raw == self.raw_database_data
        assert d.id == self.raw_database_data["id"]
        assert d.title == self.raw_database_data["title"][0]["plain_text"]
        assert d.parent == self.raw_database_data["parent"]
        assert d.url == self.raw_database_data["url"]
        assert d.archived == self.raw_database_data["archived"]

        expected_properties = nonnulls(
            get_properties(self.raw_database_data["properties"])
        )
        assert d.id_to_properties == {prop.id: prop for prop in expected_properties}
        assert d.name_to_properties == {prop.name: prop for prop in expected_properties}

    def test_get_title(self):
        title = [
            {
                "type": "text",
                "text": {"content": "Example Test", "link": None},
                "annotations": {
                    "bold": False,
                    "italic": False,
                    "strikethrough": False,
                    "underline": False,
                    "code": False,
                    "color": "default",
                },
                "plain_text": "Example Test",
                "href": None,
            },
            {
                "type": "text",
                "text": {"content": "Database Title", "link": None},
                "annotations": {
                    "bold": False,
                    "italic": False,
                    "strikethrough": False,
                    "underline": False,
                    "code": False,
                    "color": "default",
                },
                "plain_text": "Database Title",
                "href": None,
            },
        ]

        expected_title = " ".join(t["plain_text"] for t in title)
        assert Database.get_title({"title": title}) == expected_title
