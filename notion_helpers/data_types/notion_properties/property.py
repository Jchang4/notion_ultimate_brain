from enum import Enum
from typing import Any, Dict


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


class Property:
    _raw: Dict[str, Any]
    id: str
    name: str
    type: PropertyTypes
    value: Dict[str, Any]

    def __init__(self, json_data: Dict[str, Any]):
        self._raw = json_data

        self.id = self._raw["id"]
        self.name = self._raw.get("name", "")
        self.type = PropertyTypes(self._raw["type"])

        # Always run this last so we can have the above
        # properties available in self
        self.value = self.get_value(self._raw[self.type])

    def get_value(self, payload: Any):
        raise NotImplementedError()

    def __repr__(
        self,
        extra_info: str = "",
        class_name: str = "",
    ) -> str:
        str_repr = f'id="{self.id}" name="{self.name}"'
        if extra_info:
            str_repr += f" {extra_info}"
        class_name = class_name if class_name else self.__class__.__name__
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


class NotImplementedProperty(Property):
    def get_value(self, payload: Any):
        return payload

    def __repr__(self) -> str:
        return super().__repr__("NOT_IMPLEMENTED", f"{self.type.value.title()}Property")
