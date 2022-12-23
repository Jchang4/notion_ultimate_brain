from notion_client import Client

from notion_ultimate_brain.notion.__tests__.helpers import (
    TEST_DATABASE_DATA,
    TEST_PAGE_DATA,
)
from notion_ultimate_brain.notion.property import Property


class TestProperty:
    def test_create__database(self):
        notion = Client()

        actual_properties = [
            Property(notion=notion, json_data=prop, prop_name=prop_name)
            for prop_name, prop in TEST_DATABASE_DATA["properties"].items()
        ]
        for actual_prop in actual_properties:
            expected_prop = TEST_DATABASE_DATA["properties"][actual_prop.name]
            assert actual_prop._raw == expected_prop
            assert actual_prop.id == expected_prop["id"]
            assert actual_prop.name == expected_prop["name"]
            assert actual_prop.type == expected_prop["type"]
            assert actual_prop.value == expected_prop[actual_prop.type]

    def test_create__page(self):
        notion = Client()

        actual_properties = {
            prop["id"]: Property(notion=notion, json_data=prop, prop_name=prop_name)
            for prop_name, prop in TEST_PAGE_DATA["properties"].items()
        }
        for expected_prop_name, expected_prop in TEST_PAGE_DATA["properties"].items():
            actual_prop = actual_properties[expected_prop["id"]]
            assert actual_prop._raw == expected_prop
            assert actual_prop.id == expected_prop["id"]
            assert actual_prop.name == expected_prop_name
            assert actual_prop.type == expected_prop["type"]
            assert actual_prop.value == expected_prop[actual_prop.type]

    def test_get_value(self):
        notion = Client()
        expected_property = next(iter(TEST_PAGE_DATA["properties"].values()))
        actual_property = Property(
            notion=notion, json_data=expected_property, prop_name="prop_name"
        )
        assert actual_property.value == expected_property[expected_property["type"]]
