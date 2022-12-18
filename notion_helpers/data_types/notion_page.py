from typing import Any, Dict

from notion_helpers.data_types.base import NotionBase
from notion_helpers.data_types.notion_properties.all import PropertyTypes
from notion_helpers.helpers import get_plain_text_from_title


class Page(NotionBase):
    @staticmethod
    def get_title(page: Dict[str, Any]) -> str:
        title = page["properties"]["Title"]["title"]
        return get_plain_text_from_title(title)

    def __repr__(self) -> str:
        return super().__repr__(f"num_props={len(self.id_to_properties)}")


def get_property_from_page(
    page, prop_type: PropertyTypes, include_empty_value: bool = False
):
    result = {
        name: prop
        for name, prop in page["properties"].items()
        if prop["type"] == prop_type
    }
    if not include_empty_value:
        result = {name: prop for name, prop in result.items() if prop[prop_type]}
    return result


def get_property_from_pages(
    pages, prop_type: PropertyTypes, include_empty_value: bool = False
):
    result = {}
    for page in pages:
        curr = get_property_from_page(page, prop_type, include_empty_value)
        result.update(curr)
    return result
