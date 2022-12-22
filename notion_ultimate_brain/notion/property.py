from enum import Enum
from typing import Any, Dict, List, Optional

from notion_client import Client

from notion_ultimate_brain.helpers import JSON, PROPERTY_VALUE
from notion_ultimate_brain.notion.types import WithClientMixin, WithRawPayloadMixin


class PropertyTypes(str, Enum):
    TITLE = "title"
    RICH_TEXT = "rich_text"
    NUMBER = "number"
    SELECT = "select"
    MULTI_SELECT = "multi_select"
    DATE = "date"
    PEOPLE = "people"
    FILES = "files"
    CHECKBOX = "checkbox"
    URL = "url"
    EMAIL = "email"
    PHONE_NUMBER = "phone_number"
    FORMULA = "formula"
    RELATION = "relation"
    ROLLUP = "rollup"
    CREATED_TIME = "created_time"
    CREATED_BY = "created_by"
    LAST_EDITED_TIME = "last_edited_time"
    LAST_EDITED_BY = "last_edited_by"
    STATUS = "status"

    def __repr__(self) -> str:
        return f'<PropertyType "{self.value}">'


class Property(WithClientMixin, WithRawPayloadMixin):
    id: str
    name: str
    type: PropertyTypes
    value: PROPERTY_VALUE

    def __init__(self, notion: Client, json_data: JSON, prop_name: str):
        super().__init__(notion=notion, raw=json_data)

        self.id = self._raw["id"]
        self.name = self._raw.get("name", prop_name)
        self.type = PropertyTypes(self._raw["type"])

        # Always run this last so we can have the above
        # properties available in self
        self.value = self.get_value(self._raw[self.type])

    def get_value(self, payload: JSON):
        return payload

    def __repr__(
        self,
        extra_info: str = "",
        class_name: str = "",
    ) -> str:
        str_repr = f'id="{self.id}" name="{self.name}"'
        if extra_info:
            str_repr += f" {extra_info}"
        class_name = f"{self.type.value.title()}Property"
        return f"<{class_name} {str_repr}>"

    def __eq__(self, other: "Property") -> bool:
        self_props = vars(self)
        other_props = vars(other)
        if set(self_props) != set(other_props):
            return False

        for prop in self_props:
            if getattr(self, prop) != getattr(other, prop):
                return False

        return True


class WithProperties(WithClientMixin):
    id_to_property: Dict[str, Property]

    def __init__(self, properties: JSON, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.id_to_property = {}
        for prop_name, prop in properties.items():
            prop = Property(self.notion, prop, prop_name)
            self.id_to_property[prop.id] = prop

    def get_prop_by_id(self, prop_id: str) -> Property:
        return self.id_to_property[prop_id]

    def get_prop_by_name(self, prop_name: str) -> Optional[Property]:
        name_to_property = {prop.name: prop for prop in self.id_to_property.values()}
        return name_to_property.get(prop_name)

    def get_props_by_type(self, prop_type: PropertyTypes) -> List[Property]:
        return [prop for prop in self.id_to_property.values() if prop.type == prop_type]

    @property
    def properties(self) -> List[Property]:
        return list(self.id_to_property.values())
