from notion_ultimate_brain.constants import UB_AREAS_AND_RESOURCES_DATABASE
from notion_ultimate_brain.databases.base import UltimateBrainDatabase
from notion_ultimate_brain.helpers import JSON


class ResourcesDatabase(UltimateBrainDatabase):
    id: str = UB_AREAS_AND_RESOURCES_DATABASE
    base_database_query_filter: JSON = {
        "and": [{"property": "Type", "select": {"equals": "Resource"}}]
    }
