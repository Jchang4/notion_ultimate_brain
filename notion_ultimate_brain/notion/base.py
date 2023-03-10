from typing import Any, Dict, List

from notion_client import Client

from notion_ultimate_brain.helpers import JSON
from notion_ultimate_brain.notion.mixins import WithRawPayloadMixin
from notion_ultimate_brain.notion.property import WithProperties


# For Databases and Pages
class NotionBase(WithProperties, WithRawPayloadMixin):
    def __init__(self, notion: Client, data: JSON, **kargs: Any) -> None:
        super().__init__(
            notion=notion,
            raw=data,
            properties=data.get("properties", {}),
            **kargs,
        )
        self.id = data.get("id", "")
        self.title = self.format_title(data.get("title", ""))
        self.parent = data.get("parent", {})
        self.url = data.get("url", "")
        self.archived = data.get("archived", False)

    def format_title(self, title: List[JSON]) -> str:
        return self._get_plain_text_from_title(title)

    @staticmethod
    def _get_plain_text_from_title(title: List[Dict[str, Any]]) -> str:
        return " ".join([t["plain_text"] for t in title])

    def __repr__(self, extra_str: str = "", class_name: str = "") -> str:
        class_name = class_name if class_name else self.__class__.__name__
        str_repr = f'id="{self.id}" title="{self.title}"'
        if extra_str:
            str_repr += f" {extra_str}"
        return f"<{class_name} {str_repr}>"
