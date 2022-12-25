from typing import Any, Optional

from notion_client import Client

from notion_ultimate_brain.helpers import JSON
from notion_ultimate_brain.notion.all import NotionDatabase


class UltimateBrainDatabase(NotionDatabase):
    def __init__(
        self, notion: Client, data: Optional[JSON] = None, **kargs: Any
    ) -> None:
        if not data:
            data = {"id": self.id}
        super().__init__(notion=notion, data=data, **kargs)
