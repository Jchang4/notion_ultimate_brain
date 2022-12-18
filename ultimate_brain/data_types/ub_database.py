import logging
from typing import List, Optional

from notion_client import Client

from helpers import nonnulls
from notion_helpers.data_types.notion_database import Database
from ultimate_brain.constants import (
    UB_AREAS_AND_RESOURCES_DATABASE,
    UB_GOALS_DATABASE,
    UB_MILESTONES_DATABASE,
    UB_NOTES_DATABASE,
    UB_PROJECTS_DATABASE,
    UB_ROOT_BLOCK_ID,
    UB_TASKS_DATABASE,
)


class UltimateBrainDatabase(Database):
    def __init__(self, database: Database):
        for key, value in vars(database).items():
            setattr(self, key, value)


class NotesDatabase(UltimateBrainDatabase):
    pass


class MilestonesDatabase(UltimateBrainDatabase):
    pass


class ProjectsDatabase(UltimateBrainDatabase):
    pass


class TasksDatabase(UltimateBrainDatabase):
    pass


class GoalsDatabase(UltimateBrainDatabase):
    pass


class AreasAndResourcesDatabase(UltimateBrainDatabase):
    pass


def ub_database_switch(database: Database) -> Optional[UltimateBrainDatabase]:
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


def get_ub_databases(
    notion: Client, with_archived: bool = False
) -> List[UltimateBrainDatabase]:
    databases = Database.get_all_databases(notion)
    databases = [d for d in databases if d.parent.get("block_id") == UB_ROOT_BLOCK_ID]
    databases = nonnulls(map(ub_database_switch, databases))
    if with_archived:
        return databases
    return list(filter(lambda d: not d.archived, databases))
