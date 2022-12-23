from typing import Any, Dict, Optional

from notion_ultimate_brain.constants import UB_TASKS_DATABASE
from notion_ultimate_brain.databases.base import UltimateBrainDatabase
from notion_ultimate_brain.pages.all import TaskPage


class TasksDatabase(UltimateBrainDatabase):
    database_id: str = UB_TASKS_DATABASE
    id_to_page: Dict[str, TaskPage]

    def get_pages(
        self, query_filter: Optional[Dict[str, Any]] = None
    ) -> Dict[str, TaskPage]:
        super().get_pages(query_filter)
        self._page_to_task_page()
        return self.id_to_page

    def _page_to_task_page(self) -> None:
        self.id_to_page = {
            id: TaskPage(self, page._raw) for id, page in self.id_to_page.items()
        }
