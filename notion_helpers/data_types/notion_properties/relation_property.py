from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union

from helpers import find
from notion_helpers.data_types.notion_properties.property import Property


@dataclass
class RelationSource:
    database_id: str
    type: str
    dual_property_synced_property_name: str
    dual_property_synced_property_id: str


@dataclass
class RelationPropertyValue:
    linked_ids: List[str] = field(default_factory=list)
    source: Optional[RelationSource] = None


class RelationProperty(Property):
    value: RelationPropertyValue

    def get_value(
        self, payload: Union[Dict[str, Any], List[Dict[str, str]]]
    ) -> RelationPropertyValue:
        if isinstance(payload, list):
            return RelationPropertyValue(
                linked_ids=[r["id"] for r in payload],
            )
        return RelationPropertyValue(
            source=RelationSource(
                database_id=find("database_id", payload),
                type=find("type", payload),
                dual_property_synced_property_name=find(
                    "dual_property.synced_property_name", payload
                ),
                dual_property_synced_property_id=find(
                    "dual_property.synced_property_id", payload
                ),
            ),
        )

    def __repr__(self) -> str:
        return super().__repr__(f"num_linked_ids={len(self.value.linked_ids)}")
