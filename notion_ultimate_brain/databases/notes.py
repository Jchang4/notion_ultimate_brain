from notion_ultimate_brain.constants import UB_NOTES_DATABASE
from notion_ultimate_brain.databases.base import UltimateBrainDatabase


class NotesDatabase(UltimateBrainDatabase):
    id: str = UB_NOTES_DATABASE
