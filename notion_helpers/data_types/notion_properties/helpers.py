import logging
from typing import Any, Dict, List, Optional

from notion_helpers.data_types.notion_properties.date_property import (
    CreatedTimeProperty,
    DateProperty,
)
from notion_helpers.data_types.notion_properties.number_property import NumberProperty
from notion_helpers.data_types.notion_properties.property import Property, PropertyTypes
from notion_helpers.data_types.notion_properties.url_property import UrlProperty


def property_switch(raw_property: Dict[str, Any]) -> Optional[Property]:
    prop_type = PropertyTypes(raw_property["type"])
    match prop_type:
        case PropertyTypes.CREATED_TIME:
            return CreatedTimeProperty(raw_property)
        case PropertyTypes.DATE:
            return DateProperty(raw_property)
        case PropertyTypes.NUMBER:
            return NumberProperty(raw_property)
        case PropertyTypes.URL:
            return UrlProperty(raw_property)
        case _:
            logging.warn(f'Property "{prop_type.value}" has no Python class')
            return None


def get_properties(
    raw_properties: Dict[str, Dict[str, Any]]
) -> List[Optional[Property]]:
    results = []
    for name, raw_property in raw_properties.items():
        if "name" not in raw_property:
            raw_property["name"] = name
        results.append(property_switch(raw_property))
    return results
