from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, Optional, Union

from notion_helpers.data_types.notion_properties.property import Property


@dataclass
class DatePropertyValue:
    start: Optional[datetime] = None
    end: Optional[datetime] = None
    time_zone: Optional[str] = None


class DateProperty(Property):
    value: DatePropertyValue

    def get_value(self, payload: Optional[Dict[str, Any]]) -> DatePropertyValue:
        if not payload:
            return DatePropertyValue()
        return DatePropertyValue(
            start=self.from_string(payload.get("start")),
            end=self.from_string(payload.get("end")),
            time_zone=payload.get("time_zone"),
        )

    @staticmethod
    def from_string(str_date: Optional[str]) -> Optional[datetime]:
        if str_date is None:
            return None
        return datetime.fromisoformat(str_date)

    def pretty_print_date(self, date: Optional[datetime]) -> str:
        if not date:
            return "None"
        return date.strftime("%b %d %Y at %I:%M %p")

    def __repr__(self) -> str:
        date_str = f'start="{self.pretty_print_date(self.value.start)}"'
        if self.value.end:
            date_str += f' end="{self.pretty_print_date(self.value.end)}"'
        return super().__repr__(date_str)


class CreatedTimeProperty(DateProperty):
    def get_value(self, payload: Union[Dict, str]) -> DatePropertyValue:
        if isinstance(payload, dict):
            return DateProperty.get_value(self, payload)
        return DateProperty.get_value(self, {"start": payload})

    @staticmethod
    def from_string(str_date: Optional[str]) -> Optional[datetime]:
        if str_date is None:
            return None
        return DateProperty.from_string(str_date.replace("Z", ""))

    def __repr__(self) -> str:
        date_str = f'created_at="{self.pretty_print_date(self.value.start)}"'
        return Property.__repr__(self, date_str)
