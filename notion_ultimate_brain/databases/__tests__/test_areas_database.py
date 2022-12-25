from notion_ultimate_brain.databases.areas import AreasDatabase


class TestAreasDatabase:
    def test_base_database_query_filter(self):
        assert AreasDatabase.base_database_query_filter == {
            "and": [{"property": "Type", "select": {"equals": "Area"}}]
        }
