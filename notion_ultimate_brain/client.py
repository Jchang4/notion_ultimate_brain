import logging
import os
from typing import Any

from notion_client import Client

from notion_ultimate_brain.constants import (
    UB_AREAS_AND_RESOURCES_DATABASE,
    UB_GOALS_DATABASE,
    UB_MILESTONES_DATABASE,
    UB_NOTES_DATABASE,
    UB_PROJECTS_DATABASE,
    UB_TASKS_DATABASE,
)

NOTION_TOKEN = os.environ.get("NOTION_TOKEN")


class UltimateBrainNotionClient(Client):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(auth=NOTION_TOKEN, **kwargs)

        from notion_ultimate_brain.databases import get_ub_databases

        databases = get_ub_databases(self)
        for database in databases:
            self._ub_database_switch(database)

    def _ub_database_switch(self, database) -> None:
        from notion_ultimate_brain.databases import (
            AreasAndResourcesDatabase,
            GoalsDatabase,
            MilestonesDatabase,
            NotesDatabase,
            ProjectsDatabase,
            TasksDatabase,
        )

        if database.id == UB_NOTES_DATABASE:
            ub_database = NotesDatabase(database)
            self.notes = ub_database
            return
        elif database.id == UB_MILESTONES_DATABASE:
            ub_database = MilestonesDatabase(database)
            self.milestones = ub_database
            return
        elif database.id == UB_PROJECTS_DATABASE:
            ub_database = ProjectsDatabase(database)
            self.projects = ub_database
            return
        elif database.id == UB_TASKS_DATABASE:
            ub_database = TasksDatabase(database)
            self.tasks = ub_database
            return
        elif database.id == UB_GOALS_DATABASE:
            ub_database = GoalsDatabase(database)
            self.goals = ub_database
            return
        elif database.id == UB_AREAS_AND_RESOURCES_DATABASE:
            ub_database = AreasAndResourcesDatabase(database)
            self.areas_and_resources = ub_database
            return
        else:
            logging.error(
                f'Unrecognized Ultimate Brain Database: {database.id} - "{database.title}"'
            )


class WithClientMixin:
    _notion: UltimateBrainNotionClient

    def __init__(self, notion: UltimateBrainNotionClient, **kargs: Any) -> None:
        super().__init__(**kargs)
        self._notion = notion
