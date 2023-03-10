from __future__ import annotations

import logging
import os
from typing import Any, List, Optional

from notion_client import Client

from notion_ultimate_brain.constants import UB_ROOT_BLOCK_ID
from notion_ultimate_brain.databases.all import (
    AreasDatabase,
    GoalsDatabase,
    MilestonesDatabase,
    NotesDatabase,
    ProjectsDatabase,
    ResourcesDatabase,
    TasksDatabase,
    UltimateBrainDatabase,
)
from notion_ultimate_brain.notion.all import NotionDatabase

NOTION_TOKEN = os.environ.get("NOTION_TOKEN")


class UltimateBrainNotionClient(Client):
    areas: AreasDatabase
    resources: ResourcesDatabase
    goals: GoalsDatabase
    milestones: MilestonesDatabase
    notes: NotesDatabase
    projects: ProjectsDatabase
    tasks: TasksDatabase

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(auth=NOTION_TOKEN, **kwargs)
        self.areas = AreasDatabase(self)
        self.goals = GoalsDatabase(self)
        self.milestones = MilestonesDatabase(self)
        self.notes = NotesDatabase(self)
        self.projects = ProjectsDatabase(self)
        self.resources = ResourcesDatabase(self)
        self.tasks = TasksDatabase(self)

    def _ub_database_switch(
        self, database: NotionDatabase
    ) -> Optional[UltimateBrainDatabase]:
        if database.id == NotesDatabase.id:
            self.notes = NotesDatabase(self, database._raw)
            return self.notes
        elif database.id == MilestonesDatabase.id:
            self.milestones = MilestonesDatabase(self, database._raw)
            return self.milestones
        elif database.id == ProjectsDatabase.id:
            self.projects = ProjectsDatabase(self, database._raw)
            return self.projects
        elif database.id == TasksDatabase.id:
            self.tasks = TasksDatabase(self, database._raw)
            return self.tasks
        elif database.id == GoalsDatabase.id:
            self.goals = GoalsDatabase(self, database._raw)
            return self.goals
        elif database.id == AreasDatabase.id:
            self.areas = AreasDatabase(self, database._raw)
            self.resources = ResourcesDatabase(self, database._raw)
            return self.areas
        else:
            logging.error(
                f'Unrecognized Ultimate Brain Database: {database.id} - "{database.title}"'
            )

    def get_ub_databases(
        self, with_archived: bool = False, page_size: int = 10
    ) -> List[UltimateBrainDatabase]:
        databases = self.get_all_databases(page_size=page_size)
        databases = [
            self._ub_database_switch(d)
            for d in databases
            if d.parent.get("block_id") == UB_ROOT_BLOCK_ID
        ]
        if with_archived:
            return self.ub_databases
        return [db for db in self.ub_databases if not db.archived]

    def get_all_databases(
        self, query: str = "", page_size: int = 10
    ) -> List[NotionDatabase]:
        databases = self.search(
            query=query,
            filter={
                "property": "object",
                "value": "database",
            },
            page_size=page_size,
        )
        assert isinstance(databases, dict)

        return [NotionDatabase(notion=self, data=data) for data in databases["results"]]

    @property
    def ub_databases(self) -> List[UltimateBrainDatabase]:
        return [
            self.areas,
            self.resources,
            self.goals,
            self.milestones,
            self.notes,
            self.projects,
            self.tasks,
        ]
