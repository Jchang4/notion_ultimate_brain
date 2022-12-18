from dataclasses import dataclass
from typing import Any, Dict, Optional

from notion_helpers.data_types.notion_properties.property import Property


@dataclass
class RollupPropertyValue:
    rollup_property_name: Optional[str] = None
    relation_property_name: Optional[str] = None
    rollup_property_id: Optional[str] = None
    relation_property_id: Optional[str] = None
    function: Optional[str] = None

    type: Optional[str] = None
    value: Optional[Any] = None


class RollupProperty(Property):
    value: RollupPropertyValue

    def get_value(self, payload: Dict[str, Any]):
        if "rollup_property_name" in payload:
            return RollupPropertyValue(
                rollup_property_name=payload["rollup_property_name"],
                relation_property_name=payload["relation_property_name"],
                rollup_property_id=payload["rollup_property_id"],
                relation_property_id=payload["relation_property_id"],
                function=payload["function"],
            )
        rollup_type = payload["type"]
        return RollupPropertyValue(
            type=rollup_type,
            value=payload[rollup_type],
            function=payload["function"],
        )

    def __repr__(self) -> str:
        rollup_str = ""
        if self.value.relation_property_name:
            rollup_str += (
                f' relation_property_name="{self.value.relation_property_name}"'
            )
        if self.value.type:
            rollup_str += f' type="{self.value.type}"'
        if self.value.value:
            rollup_str += f' value="{self.value.value}"'
        return super().__repr__(rollup_str.strip())
