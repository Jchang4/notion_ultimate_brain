from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional

from notion_ultimate_brain.constants import UB_TASKS_DATABASE
from notion_ultimate_brain.helpers import (
    dict_by,
    get_start_and_end_of_day,
    to_notion_strftime,
)
from notion_ultimate_brain.notion.page import NotionPage
from notion_ultimate_brain.types import JSON


class WithTasks(NotionPage):
    base_task_filter: Dict[str, Any]

    def get_tasks(
        self, query_filter: Optional[List[JSON]] = None
    ) -> Dict[str, "TaskPage"]:
        from notion_ultimate_brain.databases import NotionDatabase, TasksDatabase

        task_filter = [self.base_task_filter]
        if query_filter:
            task_filter += query_filter
        print({"and": task_filter})
        response = self._notion.databases.query(
            **{
                "database_id": UB_TASKS_DATABASE,
                "filter": {"and": task_filter},
            }
        )
        assert isinstance(response, dict)
        return dict_by(
            [
                TaskPage(
                    TasksDatabase(
                        NotionDatabase(self._notion, {"id": UB_TASKS_DATABASE})
                    ),
                    page_data,
                )
                for page_data in response["results"]
            ],
            "id",
        )

    @property
    def all_tasks(self) -> Dict[str, "TaskPage"]:
        return self.get_tasks()

    def get_current_tasks(
        self,
        query_filter: Optional[List[JSON]] = None,
        include_done: bool = False,
        include_kanban_done: bool = False,
    ) -> Dict[str, "TaskPage"]:
        task_filter = []

        if not include_done:
            task_filter.append(
                {"property": "Done", "checkbox": {"equals": False}},
            )
        if not include_kanban_done:
            task_filter.append(
                {"property": "Kanban Status", "select": {"does_not_equal": "Done"}},
            )
        if query_filter:
            task_filter += query_filter

        return self.get_tasks(task_filter)

    def get_current_tasks_with_offset(
        self,
        offset_days: int = 0,
        include_done: bool = False,
        include_kanban_done: bool = False,
    ) -> Dict[str, "TaskPage"]:
        _, end_date = get_start_and_end_of_day(offset_days=offset_days)
        return self.get_current_tasks(
            [WithTasks._get_date_filter(end_date=end_date - timedelta(minutes=1))],
            include_done,
            include_kanban_done,
        )

    @property
    def yesterday_tasks(self) -> Dict[str, "TaskPage"]:
        return self.get_current_tasks_with_offset(
            -1, include_done=True, include_kanban_done=True
        )

    @property
    def today_tasks(self) -> Dict[str, "TaskPage"]:
        return self.get_current_tasks_with_offset(0)

    @property
    def tomorrow_tasks(self) -> Dict[str, "TaskPage"]:
        return self.get_current_tasks_with_offset(1)

    def get_completed_tasks(
        self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None
    ) -> Dict[str, "TaskPage"]:
        or_query_filter = [
            {"property": "Done", "checkbox": {"equals": True}},
            {"property": "Kanban Status", "select": {"equals": "Done"}},
        ]
        and_query_filter = []

        if start_date or end_date:
            and_query_filter.append(self._get_date_filter(start_date, end_date))

        return self.get_current_tasks(
            and_query_filter + [{"or": or_query_filter}],
            include_done=True,
            include_kanban_done=True,
        )

    @property
    def task_ids(self) -> List[str]:
        tasks = self.get_prop_by_name("Tasks")
        if not tasks:
            return []
        return tasks._raw["relation"]["linked_ids"]

    @staticmethod
    def _get_date_filter(
        start_date: Optional[datetime] = None, end_date: Optional[datetime] = None
    ) -> JSON:
        date_query = {}
        if start_date:
            date_query["on_or_after"] = to_notion_strftime(start_date)
        if end_date:
            date_query["on_or_before"] = to_notion_strftime(end_date)
        return {
            "property": "Due",
            "date": date_query,
        }


class TaskPage(WithTasks):
    def __init__(self, database: Any, data: JSON, **kargs: Any) -> None:
        super().__init__(database, data, **kargs)
        self.base_task_filter = {
            "property": "Parent Task",
            "relation": {
                "contains": self.id,
            },
        }
