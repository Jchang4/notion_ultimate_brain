from typing import Any, Dict, List, Optional

from notion_client import Client

from notion_ultimate_brain.helpers import JSON
from notion_ultimate_brain.notion.base import NotionBase
from notion_ultimate_brain.notion.page import NotionPage


class NotionDatabase(NotionBase):
    id_to_page: Dict[str, NotionPage]

    def __init__(self, notion: Client, data: JSON, **kargs: Any) -> None:
        super().__init__(notion=notion, data=data, **kargs)
        self.id_to_page = {}

    @property
    def pages(self) -> List[NotionPage]:
        return list(self.id_to_page.values())

    def get_pages(
        self, query_filter: Optional[Dict[str, Any]] = None
    ) -> Dict[str, NotionPage]:
        response = self.notion.databases.query(self.id, filter=query_filter)
        assert isinstance(response, dict)
        pages = []
        for data in response["results"]:
            page = NotionPage(self, data)
            pages.append(page)
        self._update_id_to_pages(pages)
        return self.id_to_page

    def _update_id_to_pages(self, pages: List[NotionPage]) -> None:
        self.id_to_page.update({page.id: page for page in pages})
