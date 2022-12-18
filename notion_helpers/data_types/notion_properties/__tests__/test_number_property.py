from notion_helpers.data_types.notion_properties.__tests__.helpers import (
    DATABASE_PROPERTY_DATA,
    PAGE_PROPERTY_DATA,
    PropertyTypes,
)
from notion_helpers.data_types.notion_properties.number_property import (
    NumberProperty,
    NumberPropertyValue,
)


class TestNumberProperty:
    raw_number_property_from_database = DATABASE_PROPERTY_DATA[PropertyTypes.NUMBER]
    raw_number_property_from_page = PAGE_PROPERTY_DATA[PropertyTypes.NUMBER]

    def test_create__no_value(self):
        """This mocks a database query where only the format is returned

        https://developers.notion.com/reference/property-object#number-configuration
        """
        actual_property = NumberProperty(self.raw_number_property_from_database)
        assert isinstance(actual_property.value, NumberPropertyValue)
        assert (
            actual_property.value.format
            == self.raw_number_property_from_database["number"]["format"]
        )
        assert actual_property.value.value == None

    def test_create__with_value(self):
        """This mocks a page query where only the value is returned

        https://developers.notion.com/reference/page-property-values#number
        """
        actual_property = NumberProperty(self.raw_number_property_from_page)
        assert isinstance(actual_property.value, NumberPropertyValue)
        assert actual_property.value.format == None
        assert (
            actual_property.value.value == self.raw_number_property_from_page["number"]
        )
