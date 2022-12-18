from notion_helpers.data_types.notion_properties.__tests__.helpers import (
    DATABASE_PROPERTY_DATA,
    PAGE_PROPERTY_DATA,
    PropertyTypes,
)
from notion_helpers.data_types.notion_properties.date_property import (
    CreatedTimeProperty,
)


class TestCreatedTimeProperty:
    raw_creation_time_property_from_database = DATABASE_PROPERTY_DATA[
        PropertyTypes.CREATED_TIME
    ]
    raw_creation_time_property_from_page = PAGE_PROPERTY_DATA[
        PropertyTypes.CREATED_TIME
    ]

    def test_create_from_database(self):
        """This mocks a database query where no date is returned

        https://developers.notion.com/reference/property-object#created-time-configuration
        """
        actual_property = CreatedTimeProperty(
            self.raw_creation_time_property_from_database
        )
        assert actual_property.value.start is None
        assert actual_property.value.end is None
        assert actual_property.value.time_zone is None

    def test_create_from_page(self):
        """This mocks a page query where only the value is returned

        https://developers.notion.com/reference/page-property-values#created-time
        """
        actual_property = CreatedTimeProperty(self.raw_creation_time_property_from_page)
        expected_creation_time_str = self.raw_creation_time_property_from_page[
            "created_time"
        ]
        assert actual_property.value.start == CreatedTimeProperty.from_string(
            expected_creation_time_str
        )
        assert actual_property.value.end is None
        assert actual_property.value.time_zone is None
