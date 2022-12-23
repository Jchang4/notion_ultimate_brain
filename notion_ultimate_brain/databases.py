from typing import Any, Dict, List, Optional

from notion_client import Client

from notion_ultimate_brain.constants import (
    UB_AREAS_AND_RESOURCES_DATABASE,
    UB_GOALS_DATABASE,
    UB_MILESTONES_DATABASE,
    UB_NOTES_DATABASE,
    UB_PROJECTS_DATABASE,
    UB_TASKS_DATABASE,
)
from notion_ultimate_brain.helpers import JSON, get_day_midnight, to_notion_strftime
from notion_ultimate_brain.notion.all import NotionDatabase, NotionPage
from notion_ultimate_brain.pages.all import ProjectPage, TaskPage


class UltimateBrainDatabase(NotionDatabase):
    database_id: str

    def __init__(
        self, notion: Client, data: Optional[JSON] = None, **kargs: Any
    ) -> None:
        if not data:
            data = {"id": self.database_id}
        super().__init__(notion, data, **kargs)


class NotesDatabase(UltimateBrainDatabase):
    database_id: str = UB_NOTES_DATABASE


class MilestonesDatabase(UltimateBrainDatabase):
    database_id: str = UB_MILESTONES_DATABASE


class ProjectsDatabase(UltimateBrainDatabase):
    database_id: str = UB_PROJECTS_DATABASE
    id_to_page: Dict[str, ProjectPage]

    def _update_id_to_pages(self, pages: List[NotionPage]) -> None:
        self.id_to_page.update(
            {page.id: ProjectPage(self, page._raw) for page in pages}
        )

    @property
    def today(self) -> Dict[str, NotionPage]:
        start = get_day_midnight()
        return self.get_pages(
            query_filter={
                "and": [
                    {
                        "property": "Status",
                        "select": {"equals": "Doing"},
                    },
                    {
                        "or": [
                            {
                                "property": "Completed",
                                "date": {
                                    "is_empty": True,
                                },
                            },
                            {
                                "property": "Completed",
                                "date": {
                                    "after": to_notion_strftime(start),
                                },
                            },
                        ]
                    },
                ]
            },
        )


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


class GoalsDatabase(UltimateBrainDatabase):
    database_id: str = UB_GOALS_DATABASE


class AreasAndResourcesDatabase(UltimateBrainDatabase):
    database_id: str = UB_AREAS_AND_RESOURCES_DATABASE
