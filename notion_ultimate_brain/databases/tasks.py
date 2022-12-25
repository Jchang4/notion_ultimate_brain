from typing import Any, Dict, List, Optional

from notion_ultimate_brain.constants import UB_TASKS_DATABASE
from notion_ultimate_brain.databases.base import UltimateBrainDatabase
from notion_ultimate_brain.notion.all import NotionPage
from notion_ultimate_brain.pages.all import TaskPage


class TasksDatabase(UltimateBrainDatabase):
    id: str = UB_TASKS_DATABASE
    id_to_page: Dict[str, TaskPage]

    def _update_id_to_pages(self, pages: List[NotionPage]) -> None:
        self.id_to_page.update({page.id: TaskPage(self, page._raw) for page in pages})
