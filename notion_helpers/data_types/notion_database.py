from typing import Any, Dict, List

from notion_client import Client

from helpers import dict_by
from notion_helpers.data_types.base import NotionBase
from notion_helpers.data_types.notion_page import Page
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

    def get_pages(self, notion: Client) -> Dict[str, Page]:
        return get_pages(notion, self.id)

    def __repr__(self) -> str:
        return super().__repr__(f"archived={self.archived}")


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


def get_pages(notion: Client, database_id: str) -> Dict[str, Page]:
    response = notion.databases.query(database_id)
    assert isinstance(response, dict)
    pages = map(Page, response["results"])
    return dict_by(list(pages), "id")
