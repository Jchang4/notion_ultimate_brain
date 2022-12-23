TEST_DATABASE_DATA = {
    "object": "database",
    "id": "notion-database-id",
    "cover": None,
    "icon": {"type": "emoji", "emoji": "🏗️"},
    "created_time": "2022-12-07T14:57:00.000Z",
    "created_by": {"object": "user", "id": "user-id-1"},
    "last_edited_by": {"object": "user", "id": "user-id-1"},
    "last_edited_time": "2022-12-07T14:57:00.000Z",
    "title": [
        {
            "type": "text",
            "text": {"content": "Notion Base Title", "link": None},
            "annotations": {
                "bold": False,
                "italic": False,
                "strikethrough": False,
                "underline": False,
                "code": False,
                "color": "default",
            },
            "plain_text": "Notion Base Title",
            "href": None,
        }
    ],
    "description": [],
    "is_inline": False,
    "properties": {
        "Archived": {
            "id": "Giws",
            "name": "Archived",
            "type": "checkbox",
            "checkbox": {},
        },
        "Status": {
            "id": "Go%3EI",
            "name": "Status",
            "type": "select",
            "select": {
                "options": [
                    {
                        "id": "select-option-1",
                        "name": "To Do",
                        "color": "blue",
                    },
                    {
                        "id": "select-option-2",
                        "name": "Doing",
                        "color": "green",
                    },
                    {
                        "id": "select-option-3",
                        "name": "Done",
                        "color": "purple",
                    },
                    {
                        "id": "select-option-4",
                        "name": "On Hold",
                        "color": "red",
                    },
                    {
                        "id": "select-option-5",
                        "name": "Ongoing",
                        "color": "orange",
                    },
                ]
            },
        },
        "Created": {
            "id": "HQ%7B%5E",
            "name": "Created",
            "type": "created_time",
            "created_time": {},
        },
        "Target Deadline": {
            "id": "JsIf",
            "name": "Target Deadline",
            "type": "date",
            "date": {},
        },
        "Completed": {"id": "Of~%7B", "name": "Completed", "type": "date", "date": {}},
        "Tasks": {
            "id": "fyxc",
            "name": "Tasks",
            "type": "relation",
            "relation": {
                "database_id": "task-database-id",
                "type": "dual_property",
                "dual_property": {
                    "synced_property_name": "Project",
                    "synced_property_id": "a~%7Cl",
                },
            },
        },
        "Name": {"id": "title", "name": "Name", "type": "title", "title": {}},
    },
    "parent": {"type": "block_id", "block_id": "notion-base-parent-id"},
    "url": "https://www.notion.so/some-notion-id",
    "archived": False,
}


TEST_PAGE_DATA = {
    "object": "page",
    "id": "notion-page-id",
    "created_time": "2022-12-20T16:37:00.000Z",
    "last_edited_time": "2022-12-22T15:58:00.000Z",
    "created_by": {"object": "user", "id": "user-id-1"},
    "last_edited_by": {"object": "user", "id": "user-id-1"},
    "cover": {
        "type": "external",
        "external": {"url": "https://google.com"},
    },
    "icon": {
        "type": "file",
        "file": {
            "url": "https://google.com",
            "expiry_time": "2022-12-23T05:07:14.101Z",
        },
    },
    "parent": {
        "type": "database_id",
        "database_id": "parent-database-id",
    },
    "archived": False,
    "properties": {
        "Archived": {"id": "Giws", "type": "checkbox", "checkbox": False},
        "Status": {
            "id": "Go%3EI",
            "type": "select",
            "select": {
                "id": "select-option-1",
                "name": "Ongoing",
                "color": "orange",
            },
        },
        "Created": {
            "id": "HQ%7B%5E",
            "type": "created_time",
            "created_time": "2022-12-20T16:37:00.000Z",
        },
        "Target Deadline": {"id": "JsIf", "type": "date", "date": None},
        "Priority": {"id": "L%5CQO", "type": "checkbox", "checkbox": True},
        "Completed": {"id": "Of~%7B", "type": "date", "date": None},
        "Tasks": {
            "id": "fyxc",
            "type": "relation",
            "relation": [
                {"id": "my-task-id-1"},
                {"id": "my-task-id-2"},
                {"id": "my-task-id-3"},
            ],
            "has_more": False,
        },
        "Name": {
            "id": "title",
            "type": "title",
            "title": [
                {
                    "type": "text",
                    "text": {"content": "Reduce Usage", "link": None},
                    "annotations": {
                        "bold": False,
                        "italic": False,
                        "strikethrough": False,
                        "underline": False,
                        "code": False,
                        "color": "default",
                    },
                    "plain_text": "Reduce Usage",
                    "href": None,
                }
            ],
        },
    },
    "url": "https://www.notion.so/some-notion-id",
}
