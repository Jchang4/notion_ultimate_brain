from __future__ import annotations

import logging
import os
from typing import Any, List, Optional

from notion_client import Client

from notion_ultimate_brain.constants import UB_ROOT_BLOCK_ID
from notion_ultimate_brain.databases import (
    AreasAndResourcesDatabase,
    GoalsDatabase,
    MilestonesDatabase,
    NotesDatabase,
    NotionDatabase,
    ProjectsDatabase,
    TasksDatabase,
    UltimateBrainDatabase,
)
from notion_ultimate_brain.helpers import nonnulls

NOTION_TOKEN = os.environ.get("NOTION_TOKEN")


class UltimateBrainNotionClient(Client):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(auth=NOTION_TOKEN, **kwargs)

    def _ub_database_switch(
        self, database: NotionDatabase
    ) -> Optional[UltimateBrainDatabase]:
        if database.id == NotesDatabase.database_id:
            ub_database = NotesDatabase(self, database._raw)
            self.notes = ub_database
            return ub_database
        elif database.id == MilestonesDatabase.database_id:
            ub_database = MilestonesDatabase(self, database._raw)
            self.milestones = ub_database
            return ub_database
        elif database.id == ProjectsDatabase.database_id:
            ub_database = ProjectsDatabase(self, database._raw)
            self.projects = ub_database
            return ub_database
        elif database.id == TasksDatabase.database_id:
            ub_database = TasksDatabase(self, database._raw)
            self.tasks = ub_database
            return ub_database
        elif database.id == GoalsDatabase.database_id:
            ub_database = GoalsDatabase(self, database._raw)
            self.goals = ub_database
            return ub_database
        elif database.id == AreasAndResourcesDatabase.database_id:
            ub_database = AreasAndResourcesDatabase(self, database._raw)
            self.areas_and_resources = ub_database
            return ub_database
        else:
            logging.error(
                f'Unrecognized Ultimate Brain Database: {database.id} - "{database.title}"'
            )

    def get_ub_databases(
        self, with_archived: bool = False, page_size: int = 10
    ) -> List[UltimateBrainDatabase]:
        databases = self.get_all_databases(page_size=page_size)
        databases = [
            d for d in databases if d.parent.get("block_id") == UB_ROOT_BLOCK_ID
        ]
        databases = nonnulls(map(self._ub_database_switch, databases))
        if with_archived:
            return databases
        return [db for db in databases if not db.archived]

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
