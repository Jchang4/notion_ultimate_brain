from typing import Dict, List

from notion_ultimate_brain.constants import UB_PROJECTS_DATABASE
from notion_ultimate_brain.databases.base import UltimateBrainDatabase
from notion_ultimate_brain.helpers import get_day_midnight, to_notion_strftime
from notion_ultimate_brain.notion.all import NotionPage
from notion_ultimate_brain.pages.project import ProjectPage


class ProjectsDatabase(UltimateBrainDatabase):
    id: str = UB_PROJECTS_DATABASE
    id_to_page: Dict[str, ProjectPage]

    def _update_id_to_pages(self, pages: List[NotionPage]) -> None:
        self.id_to_page.update(
            {page.id: ProjectPage(self, page._raw) for page in pages}
        )

    @property
    def today(self) -> Dict[str, NotionPage]:
        start = get_day_midnight()
        return self.get_pages(
            query_filter={
                "and": [
                    {
                        "property": "Status",
                        "select": {"equals": "Doing"},
                    },
                    {
                        "or": [
                            {
                                "property": "Completed",
                                "date": {
                                    "is_empty": True,
                                },
                            },
                            {
                                "property": "Completed",
                                "date": {
                                    "after": to_notion_strftime(start),
                                },
                            },
                        ]
                    },
                ]
            },
        )
