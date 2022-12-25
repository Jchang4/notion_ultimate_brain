from notion_ultimate_brain.databases.resources import ResourcesDatabase


class TestResourcesDatabase:
    def test_base_database_query_filter(self):
        assert ResourcesDatabase.base_database_query_filter == {
            "and": [{"property": "Type", "select": {"equals": "Resource"}}]
        }
