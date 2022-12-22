from typing import Any, List

from notion_ultimate_brain.helpers import JSON, flatten
from notion_ultimate_brain.notion.base import NotionBase
from notion_ultimate_brain.notion.helpers import get_plain_text_from_title
from notion_ultimate_brain.notion.property import PropertyTypes


class NotionPage(NotionBase):
    def __init__(self, database: Any, data: JSON, **kargs: Any) -> None:
        from notion_ultimate_brain.notion.database import NotionDatabase

        assert isinstance(database, NotionDatabase)

        super().__init__(database.notion, data, **kargs)

        self.database = database

    def format_title(self, _: List[JSON]) -> str:
        titles = self.get_props_by_type(PropertyTypes.TITLE)
        titles = [t._raw["title"] for t in titles]
        titles = flatten(titles)
        return get_plain_text_from_title(titles)
    