import asyncio
from typing import Any, Dict, List

from notion_client import Client

from notion_helpers.helpers import get_plain_text_from_title


class Database:
    _raw: Dict[str, Any]

    id: str
    title: str
    parent: Dict[str, Any]
    url: str
    archived: bool
    properties: Dict[str, Any]

    def __init__(self, json_data: Dict[str, Any]):
        self._raw = json_data

        self.id = self._raw["id"]
        self.title = self.get_database_title(self._raw)
        self.parent = self._raw["parent"]
        self.url = self._raw["url"]
        self.archived = self._raw["archived"]
        self.properties = self._raw["properties"]

    @staticmethod
    def get_database_title(database: Dict[str, Any]) -> str:
        return get_plain_text_from_title(database["title"])

    @staticmethod
    def get_all_databases(
        notion: Client, query: str = "", page_size: int = 10
    ) -> List["Database"]:
        databases = notion.search(
            query=query,
            filter={
                "property": "object",
                "value": "database",
            },
            page_size=page_size,
        )
        assert isinstance(databases, dict)
        return [Database(r) for r in databases["results"]]

    def __repr__(self) -> str:
        db_repr = f'id="{self.id}" title="{self.title}" archived={self.archived}'

        if issubclass(self.__class__, Database):
            return db_repr

        return f"<Database {db_repr}>"
