from datetime import datetime

from notion_helpers.data_types.notion_properties.__tests__.helpers import (
    DATABASE_PROPERTY_DATA,
    PropertyTypes,
)

DATABASE_DATA = [
    {
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
        "properties": {
            DATABASE_PROPERTY_DATA[PropertyTypes.DATE]["name"]: DATABASE_PROPERTY_DATA[
                PropertyTypes.DATE
            ],
            DATABASE_PROPERTY_DATA[PropertyTypes.CREATED_TIME][
                "name"
            ]: DATABASE_PROPERTY_DATA[PropertyTypes.CREATED_TIME],
            DATABASE_PROPERTY_DATA[PropertyTypes.URL]["name"]: DATABASE_PROPERTY_DATA[
                PropertyTypes.URL
            ],
        },
        "url": "https://www.typed-notion-is-best-notion.com",
        "archived": False,
    }
]
