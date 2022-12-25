from typing import Dict

from notion_ultimate_brain.databases.projects import ProjectsDatabase
from notion_ultimate_brain.helpers import JSON
from notion_ultimate_brain.notion.all import NotionPage
from notion_ultimate_brain.pages.project import ProjectPage


class AreaPage(NotionPage):
    def get_projects(self) -> Dict[str, ProjectPage]:
        projects_db = ProjectsDatabase(self.notion)
        projects_db.get_pages(
            query_filter={
                "and": [{"property": "Area", "relation": {"contains": self.id}}]
            }
        )
        return projects_db.id_to_page
