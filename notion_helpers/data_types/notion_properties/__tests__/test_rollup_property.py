from helpers import find
from notion_helpers.data_types.notion_properties.__tests__.helpers import (
    DATABASE_PROPERTY_DATA, PAGE_PROPERTY_DATA, PropertyTypes)
from notion_helpers.data_types.notion_properties.rollup_property import \
    RollupProperty


class TestRollupProperty:
    raw_json_from_database = DATABASE_PROPERTY_DATA[PropertyTypes.ROLLUP]
    raw_json_from_page = PAGE_PROPERTY_DATA[PropertyTypes.ROLLUP]

    def test_create_from_database(self):
        for raw_json in self.raw_json_from_database.values():
            actual = RollupProperty(raw_json)
            assert actual.type == PropertyTypes.ROLLUP
            assert actual.value.type is None
            assert actual.value.value is None

            raw_prop = raw_json["rollup"]
            assert actual.value.rollup_property_name == raw_prop["rollup_property_name"]
            assert (
                actual.value.relation_property_name
                == raw_prop["relation_property_name"]
            )
            assert actual.value.rollup_property_id == raw_prop["rollup_property_id"]
            assert actual.value.relation_property_id == raw_prop["relation_property_id"]
            assert actual.value.function == raw_prop["function"]

    def test_create_from_page(self):
        for raw_json in self.raw_json_from_page.values():
            actual = RollupProperty(raw_json)
            assert actual.type == PropertyTypes.ROLLUP
            assert actual.value.rollup_property_name is None
            assert actual.value.relation_property_name is None
            assert actual.value.rollup_property_id is None
            assert actual.value.relation_property_id is None
            
            raw_prop = raw_json["rollup"]
            raw_rollup_type = raw_prop['type']
            assert actual.value.type == raw_rollup_type
            assert actual.value.value == raw_prop[raw_rollup_type]
            assert actual.value.function == raw_prop['function']
