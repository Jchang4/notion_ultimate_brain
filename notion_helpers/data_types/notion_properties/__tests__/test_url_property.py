from notion_helpers.data_types.notion_properties.__tests__.helpers import (
    DATABASE_PROPERTY_DATA, PAGE_PROPERTY_DATA, PropertyTypes)
from notion_helpers.data_types.notion_properties.url_property import \
    UrlProperty


class TestUrlProperty:
    raw_url_property_data_from_database = DATABASE_PROPERTY_DATA[PropertyTypes.URL]
    raw_url_property_data_from_page = PAGE_PROPERTY_DATA[PropertyTypes.URL]

    def test_create_from_database(self):
        actual_property = UrlProperty(self.raw_url_property_data_from_database)
        assert actual_property.value == ""

    def test_create_from_page(self):
        actual_property = UrlProperty(self.raw_url_property_data_from_page)
        assert actual_property.value == self.raw_url_property_data_from_page["url"]