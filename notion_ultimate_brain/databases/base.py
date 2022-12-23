from typing import Any, Optional

from notion_client import Client

from notion_ultimate_brain.helpers import JSON
from notion_ultimate_brain.notion.all import NotionDatabase


class UltimateBrainDatabase(NotionDatabase):
    database_id: str

    def __init__(
        self, notion: Client, data: Optional[JSON] = None, **kargs: Any
    ) -> None:
        if not data:
            data = {"id": self.database_id}
        super().__init__(notion, data, **kargs)
