import logging
from typing import Any, Dict, List, Optional

from notion_ultimate_brain.constants import (
    UB_AREAS_AND_RESOURCES_DATABASE,
    UB_GOALS_DATABASE,
    UB_MILESTONES_DATABASE,
    UB_NOTES_DATABASE,
    UB_PROJECTS_DATABASE,
    UB_ROOT_BLOCK_ID,
    UB_TASKS_DATABASE,
)
from notion_ultimate_brain.helpers import get_day_midnight, nonnulls, to_notion_strftime
from notion_ultimate_brain.notion.database import NotionDatabase
from notion_ultimate_brain.notion.page import NotionPage
from notion_ultimate_brain.pages.project import ProjectPage
from notion_ultimate_brain.pages.task import TaskPage


class UltimateBrainDatabase(NotionDatabase):
    def __init__(self, database: NotionDatabase):
        for key, value in vars(database).items():
            setattr(self, key, value)


class NotesDatabase(UltimateBrainDatabase):
    pass


class MilestonesDatabase(UltimateBrainDatabase):
    pass


class ProjectsDatabase(UltimateBrainDatabase):
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
    pass


class AreasAndResourcesDatabase(UltimateBrainDatabase):
    pass


def ub_database_switch(database: NotionDatabase) -> Optional[UltimateBrainDatabase]:
    if database.id == UB_NOTES_DATABASE:
        return NotesDatabase(database)
    elif database.id == UB_MILESTONES_DATABASE:
        return MilestonesDatabase(database)
    elif database.id == UB_PROJECTS_DATABASE:
        return ProjectsDatabase(database)
    elif database.id == UB_TASKS_DATABASE:
        return TasksDatabase(database)
    elif database.id == UB_GOALS_DATABASE:
        return GoalsDatabase(database)
    elif database.id == UB_AREAS_AND_RESOURCES_DATABASE:
        return AreasAndResourcesDatabase(database)
    else:
        logging.warn(
            f'Unrecognized Ultimate Brain Database: {database.id} - "{database.title}"'
        )
        return None


from notion_ultimate_brain.client import UltimateBrainNotionClient


def get_all_databases(
    notion: UltimateBrainNotionClient, query: str = "", page_size: int = 10
) -> List[NotionDatabase]:

    databases = notion.search(
        query=query,
        filter={
            "property": "object",
            "value": "database",
        },
        page_size=page_size,
    )
    assert isinstance(databases, dict)

    return [NotionDatabase(notion=notion, data=data) for data in databases["results"]]


def get_ub_databases(
    notion: UltimateBrainNotionClient, with_archived: bool = False
) -> List[UltimateBrainDatabase]:
    databases = get_all_databases(notion)
    databases = [d for d in databases if d.parent.get("block_id") == UB_ROOT_BLOCK_ID]
    databases = nonnulls(map(ub_database_switch, databases))
    if with_archived:
        return databases
    return [db for db in databases if not db.archived]
