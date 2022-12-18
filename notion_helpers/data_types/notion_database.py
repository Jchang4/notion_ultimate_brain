from typing import Any, Dict, List

from notion_client import Client

from notion_helpers.data_types.base import NotionBase
from notion_helpers.data_types.notion_properties.all import PropertyTypes
from notion_helpers.helpers import get_plain_text_from_title


class Database(NotionBase):
    @staticmethod
    def get_title(database: Dict[str, Any]) -> str:
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
        parent_repr = super().__repr__()
        db_repr = f"{parent_repr} archived={self.archived}"
        if issubclass(self.__class__, Database):
            return db_repr
        return f"<Database {db_repr}>"


def get_property_from_database(database: Database, prop_type: PropertyTypes):
    return {
        name: prop
        for name, prop in database._raw["properties"].items()
        if prop["type"] == prop_type
    }


def get_property_from_databases(databases, prop_type: PropertyTypes):
    result = {}
    for database in databases:
        result.update(get_property_from_database(database, prop_type))
    return result


def get_pages(notion: Client, database_id: str) -> Dict[str, Any]:
    response = notion.databases.query(database_id)
    assert isinstance(response, dict)
    return response["results"]
