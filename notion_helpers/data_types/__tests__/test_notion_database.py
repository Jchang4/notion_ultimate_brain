from datetime import datetime

from notion_helpers.data_types.notion_database import Database


class TestDatabase:
    raw_database_data = {
        "object": "database",
        "id": "123456",
        "cover": None,
        "icon": None,
        "parent": {},
        "title": [
            {
                "type": "text",
                "text": {"content": "Example Test Database Title", "link": None},
                "annotations": {
                    "bold": False,
                    "italic": False,
                    "strikethrough": False,
                    "underline": False,
                    "code": False,
                    "color": "default",
                },
                "plain_text": "All Notes [UB]",
                "href": None,
            },
        ],
        "description": [],
        "created_by": {"object": "user", "id": "user_id_1"},
        "last_edited_by": {"object": "user", "id": "user_id_1"},
        "last_edited_time": datetime.now().isoformat(),
        "properties": {},
        "url": "https://www.typed-notion-is-best-notion.com",
        "archived": False,
    }

    def test_create_database_from_raw(self):
        d = Database(self.raw_database_data)
        assert d._raw == self.raw_database_data
        database_vars = [v for v in vars(d).keys() if v != "_raw" and v != "title"]

        for v in database_vars:
            assert getattr(d, v) == self.raw_database_data[v]

        assert d.title == self.raw_database_data["title"][0]["plain_text"]

    def test_get_database_title(self):
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
        assert Database.get_database_title({"title": title}) == expected_title
