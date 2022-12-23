from notion_ultimate_brain.constants import UB_AREAS_AND_RESOURCES_DATABASE
from notion_ultimate_brain.databases.base import UltimateBrainDatabase


class ResourcesDatabase(UltimateBrainDatabase):
    database_id: str = UB_AREAS_AND_RESOURCES_DATABASE
