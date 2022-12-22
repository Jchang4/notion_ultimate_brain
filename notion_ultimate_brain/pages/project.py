from typing import Any

from notion_ultimate_brain.helpers import JSON
from notion_ultimate_brain.pages.task import WithTasks


class ProjectPage(WithTasks):
    def __init__(self, database: Any, data: JSON, **kargs: Any) -> None:
        super().__init__(database, data, **kargs)
        self.base_task_filter = {
            "property": "Project",
            "relation": {"contains": self.id},
        }
