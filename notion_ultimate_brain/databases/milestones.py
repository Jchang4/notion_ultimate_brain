from notion_ultimate_brain.constants import UB_MILESTONES_DATABASE
from notion_ultimate_brain.databases.base import UltimateBrainDatabase


class MilestonesDatabase(UltimateBrainDatabase):
    id: str = UB_MILESTONES_DATABASE
