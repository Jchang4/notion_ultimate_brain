from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional

import notion_ultimate_brain.databases as databases
from notion_ultimate_brain.constants import UB_TASKS_DATABASE
from notion_ultimate_brain.helpers import (
    JSON,
    dict_by,
    get_start_and_end_of_day,
    query_filter_merge,
    to_notion_strftime,
)
from notion_ultimate_brain.notion.all import NotionPage


class WithTasks(NotionPage):
    base_task_filter: Dict[str, Any]

    def get_tasks(self, query_filter: Optional[JSON] = None) -> Dict[str, "TaskPage"]:
        task_filter = query_filter_merge(
            {"and": [self.base_task_filter]},
            query_filter if query_filter else {},
        )
        response = self.notion.databases.query(
            **{
                "database_id": UB_TASKS_DATABASE,
                "filter": task_filter,
            }
        )
        assert isinstance(response, dict)
        return dict_by(
            [
                TaskPage(
                    databases.TasksDatabase(self.notion, {"id": UB_TASKS_DATABASE}),
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
        query_filter: Optional[JSON] = None,
        include_done: bool = False,
        include_kanban_done: bool = False,
    ) -> Dict[str, "TaskPage"]:
        task_filter = {"and": []}

        if not include_done:
            task_filter["and"].append(
                {"property": "Done", "checkbox": {"equals": False}},
            )
        if not include_kanban_done:
            task_filter["and"].append(
                {"property": "Kanban Status", "select": {"does_not_equal": "Done"}},
            )
        if query_filter:
            task_filter = query_filter_merge(task_filter, query_filter)

        return self.get_tasks(task_filter)

    def get_current_tasks_with_offset(
        self,
        offset_days: int = 0,
        include_done: bool = False,
        include_kanban_done: bool = False,
    ) -> Dict[str, "TaskPage"]:
        _, end_date = get_start_and_end_of_day(offset_days=offset_days)
        return self.get_current_tasks(
            {
                "and": [
                    WithTasks._get_date_filter(end_date=end_date - timedelta(minutes=1))
                ]
            },
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
        task_filter = {
            "or": [
                {"property": "Done", "checkbox": {"equals": True}},
                {"property": "Kanban Status", "select": {"equals": "Done"}},
            ],
            "and": [],
        }

        if start_date or end_date:
            task_filter["and"].append(self._get_date_filter(start_date, end_date))

        return self.get_current_tasks(
            task_filter,
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
