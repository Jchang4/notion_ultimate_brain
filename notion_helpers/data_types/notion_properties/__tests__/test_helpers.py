from helpers import nonnulls, pipe
from notion_helpers.data_types.notion_properties.__tests__.helpers import (
    DATABASE_PROPERTY_DATA, PAGE_PROPERTY_DATA, PropertyTypes)
from notion_helpers.data_types.notion_properties.all import (
    CreatedTimeProperty, DateProperty, NumberProperty, UrlProperty)
from notion_helpers.data_types.notion_properties.helpers import get_properties


class TestNotionPropertyHelpers:
    raw_properties_data = {
        PropertyTypes.DATE: dict(
            database=DATABASE_PROPERTY_DATA[PropertyTypes.DATE],
            page=PAGE_PROPERTY_DATA[PropertyTypes.DATE],
        ),
        PropertyTypes.CREATED_TIME: dict(
            database=DATABASE_PROPERTY_DATA[PropertyTypes.CREATED_TIME],
            page=PAGE_PROPERTY_DATA[PropertyTypes.CREATED_TIME],
        ),
        PropertyTypes.NUMBER: dict(
            database=DATABASE_PROPERTY_DATA[PropertyTypes.NUMBER],
            page=PAGE_PROPERTY_DATA[PropertyTypes.NUMBER],
        ),
        PropertyTypes.URL: dict(
            database=DATABASE_PROPERTY_DATA[PropertyTypes.URL],
            page=PAGE_PROPERTY_DATA[PropertyTypes.URL],
        ),
    }

    def test_get_properties(self):
        for prop_type, container in self.raw_properties_data.items():
            properties = get_properties(
                {
                    f"{prop_type}__{obj_type}": data
                    for obj_type, data in container.items()
                }
            )
            for property in properties:
                match prop_type:
                    case PropertyTypes.DATE:
                        expected_class = DateProperty
                    case PropertyTypes.CREATED_TIME:
                        expected_class = CreatedTimeProperty
                    case PropertyTypes.NUMBER:
                        expected_class = NumberProperty
                    case PropertyTypes.URL:
                        expected_class = UrlProperty
                    case _:
                        raise KeyError(f"No raw data for property {prop_type}")
                assert isinstance(property, expected_class)