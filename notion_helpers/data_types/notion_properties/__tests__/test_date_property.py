from notion_helpers.data_types.notion_properties.__tests__.helpers import (
    DATABASE_PROPERTY_DATA,
    PAGE_PROPERTY_DATA,
    PropertyTypes,
)
from notion_helpers.data_types.notion_properties.date_property import DateProperty


class TestDateProperty:
    raw_date_property_from_database = DATABASE_PROPERTY_DATA[PropertyTypes.DATE]
    raw_date_property_from_page = PAGE_PROPERTY_DATA[PropertyTypes.DATE]

    def test_create_from_database(self):
        """This mocks a database query where no date is returned

        https://developers.notion.com/reference/property-object#date-configuration
        """
        actual_property = DateProperty(self.raw_date_property_from_database)
        assert actual_property._raw == self.raw_date_property_from_database
        assert actual_property.value.start is None
        assert actual_property.value.end is None
        assert actual_property.value.time_zone is None

    def test_create_from_page(self):
        """This mocks a page query where only the value is returned

        https://developers.notion.com/reference/page-property-values#date
        """
        actual_property = DateProperty(self.raw_date_property_from_page)
        assert actual_property._raw == self.raw_date_property_from_page
        assert actual_property.name == ""
        assert actual_property.value.start == DateProperty.from_string(
            self.raw_date_property_from_page["date"]["start"]
        )
        assert actual_property.value.end == (
            DateProperty.from_string(self.raw_date_property_from_page["date"]["end"])
            if self.raw_date_property_from_page["date"]["end"]
            else None
        )
        assert (
            actual_property.value.time_zone
            == self.raw_date_property_from_page["date"]["time_zone"]
        )
