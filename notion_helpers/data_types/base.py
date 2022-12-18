from typing import Any, Dict, List

from helpers import dict_by, nonnulls, pipe
from notion_helpers.data_types.notion_properties.all import Property
from notion_helpers.data_types.notion_properties.helpers import get_properties


# For Databases and Pages
class NotionBase:
    _raw: Dict[str, Any]

    id: str
    title: str
    parent: Dict[str, Any]
    url: str
    archived: bool
    id_to_properties: Dict[str, Property]
    name_to_properties: Dict[str, Property]

    def __init__(self, json_data: Dict[str, Any]):
        self._raw = json_data

        self.id = self._raw["id"]
        self.title = self.get_title(self._raw)
        self.parent = self._raw["parent"]
        self.url = self._raw["url"]
        self.archived = self._raw["archived"]
        self.id_to_properties = dict_by(
            pipe(get_properties, nonnulls)(self._raw["properties"]), "id"
        )
        self.name_to_properties = dict_by(
            pipe(get_properties, nonnulls)(self._raw["properties"]), "name"
        )

    @property
    def properties(self) -> List[Property]:
        return list(self.id_to_properties.values())

    @staticmethod
    def get_title(json_data: Dict[str, Any]) -> str:
        raise NotImplementedError()

    def __repr__(self, extra_str: str = "", class_name: str = "") -> str:
        class_name = class_name if class_name else self.__class__.__name__
        str_repr = f'id="{self.id}" title="{self.title}"'
        if extra_str:
            str_repr += f" {extra_str}"
        return f"<{class_name} {str_repr}>"
