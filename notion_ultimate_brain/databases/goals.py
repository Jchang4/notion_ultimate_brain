from notion_ultimate_brain.constants import UB_GOALS_DATABASE
from notion_ultimate_brain.databases.base import UltimateBrainDatabase


class GoalsDatabase(UltimateBrainDatabase):
    id: str = UB_GOALS_DATABASE
