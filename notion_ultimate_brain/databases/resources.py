from typing import Dict, List

from notion_ultimate_brain.constants import UB_AREAS_AND_RESOURCES_DATABASE
from notion_ultimate_brain.databases.base import UltimateBrainDatabase
from notion_ultimate_brain.helpers import JSON
from notion_ultimate_brain.notion.all import NotionPage
from notion_ultimate_brain.pages.resource import ResourcePage


class ResourcesDatabase(UltimateBrainDatabase):
    id: str = UB_AREAS_AND_RESOURCES_DATABASE
    id_to_page: Dict[str, ResourcePage]
    base_database_query_filter: JSON = {
        "and": [{"property": "Type", "select": {"equals": "Resource"}}]
    }

    def _update_id_to_pages(self, pages: List[NotionPage]) -> None:
        self.id_to_page.update(
            {page.id: ResourcePage(self, page._raw) for page in pages}
        )
