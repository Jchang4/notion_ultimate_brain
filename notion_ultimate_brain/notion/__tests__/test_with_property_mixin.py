from notion_client import Client

from notion_ultimate_brain.notion.__tests__.helpers import (
    TEST_DATABASE_DATA,
    TEST_PAGE_DATA,
)
from notion_ultimate_brain.notion.property import Property, WithProperties


class TestWithProperties:
    def test_create__database(self):
        notion = Client()
        mixin = WithProperties(
            notion=notion, properties=TEST_DATABASE_DATA["properties"]
        )
        assert mixin.notion == notion
        assert len(mixin.id_to_property) == len(TEST_DATABASE_DATA["properties"])
        for prop_id, prop in mixin.id_to_property.items():
            assert isinstance(prop, Property)
            assert prop.id == prop_id
            assert prop._raw == TEST_DATABASE_DATA["properties"][prop.name]

    def test_create__page(self):
        notion = Client()
        mixin = WithProperties(notion=notion, properties=TEST_PAGE_DATA["properties"])
        assert mixin.notion == notion
        assert len(mixin.id_to_property) == len(TEST_PAGE_DATA["properties"])
        for prop_id, prop in mixin.id_to_property.items():
            assert isinstance(prop, Property)
            assert prop.id == prop_id
            assert prop._raw == TEST_PAGE_DATA["properties"][prop.name]

    def test_get_prop_by_id(self):
        notion = Client()

        mixin = WithProperties(
            notion=notion, properties=TEST_DATABASE_DATA["properties"]
        )
        for prop_name, prop in TEST_DATABASE_DATA["properties"].items():
            actual_prop = mixin.get_prop_by_id(prop["id"])
            assert actual_prop == Property(
                notion=notion, json_data=prop, prop_name=prop_name
            )

    def test_get_prop_by_name(self):
        notion = Client()

        # Database
        mixin = WithProperties(
            notion=notion, properties=TEST_DATABASE_DATA["properties"]
        )
        for prop_name, prop in TEST_DATABASE_DATA["properties"].items():
            actual_prop = mixin.get_prop_by_name(prop_name)
            assert actual_prop == Property(
                notion=notion, json_data=prop, prop_name=prop_name
            )

        # Page
        mixin = WithProperties(notion=notion, properties=TEST_PAGE_DATA["properties"])
        for prop_name, prop in TEST_PAGE_DATA["properties"].items():
            actual_prop = mixin.get_prop_by_name(prop_name)
            assert actual_prop == Property(
                notion=notion, json_data=prop, prop_name=prop_name
            )

    def test_get_props_by_type(self):
        notion = Client()

        mixin = WithProperties(
            notion=notion, properties=TEST_DATABASE_DATA["properties"]
        )
        for prop_name, prop in TEST_DATABASE_DATA["properties"].items():
            actual_props = mixin.get_props_by_type(prop["type"])
            assert (
                Property(notion=notion, json_data=prop, prop_name=prop_name)
                in actual_props
            )

    def test_properties(self):
        notion = Client()
        mixin = WithProperties(notion=notion, properties=TEST_PAGE_DATA["properties"])
        actual_props = mixin.properties
        for actual_prop in actual_props:
            expected_prop = TEST_PAGE_DATA["properties"][actual_prop.name]
            assert actual_prop.id == expected_prop["id"]
            assert actual_prop._raw == expected_prop
