from unittest.mock import MagicMock

import pytest
from pytest_mock import MockerFixture

from notion_ultimate_brain.databases.tasks import TasksDatabase
from notion_ultimate_brain.helpers import (get_start_and_end_of_day, timedelta,
                                           to_notion_strftime)
from notion_ultimate_brain.notion.__tests__.helpers import (
    TEST_PAGE_DATA, notion_client_fixture)
from notion_ultimate_brain.notion.all import NotionPage
from notion_ultimate_brain.pages.task import TaskPage, WithTasksMixin


@pytest.fixture(name='get_tasks')
def get_tasks_fixture(mocker: MockerFixture) -> MagicMock:
    get_tasks = mocker.patch(
        "notion_ultimate_brain.pages.task.WithTasksMixin.get_tasks", return_value={}
    )
    return get_tasks


@pytest.fixture()
def get_expected_base_task_filter():
    return lambda page_id: {
        "property": "Parent Task",
        "relation": {
            "contains": page_id,
        },
    }


class TestTaskPage:
    def test_create(self, notion: MagicMock):
        page = TaskPage(TasksDatabase(notion), TEST_PAGE_DATA)
        assert isinstance(page, NotionPage)
        assert page.id == TEST_PAGE_DATA["id"]
        assert page._raw == TEST_PAGE_DATA

    def test_base_task_filter(self, notion: MagicMock, get_expected_base_task_filter):
        expected_base_task_filter = get_expected_base_task_filter(TEST_PAGE_DATA["id"])
        page = TaskPage(TasksDatabase(notion), TEST_PAGE_DATA)
        assert page.base_task_filter == expected_base_task_filter


class TestWithTasksMixin:
    def test_create(self, notion: MagicMock):
        page = WithTasksMixin(TasksDatabase(notion), TEST_PAGE_DATA)
        assert isinstance(page, NotionPage)
        assert page.id == TEST_PAGE_DATA["id"]
        assert page._raw == TEST_PAGE_DATA

    def test_get_tasks__basic(self, notion: MagicMock, get_expected_base_task_filter):
        page = WithTasksMixin(TasksDatabase(notion), TEST_PAGE_DATA)
        expected_base_task_filter = get_expected_base_task_filter(TEST_PAGE_DATA["id"])
        page.base_task_filter = expected_base_task_filter
        child_tasks = page.get_tasks()
        notion.databases.query.assert_called_once_with(
            database_id=TasksDatabase.id,
            filter={"and": [expected_base_task_filter], "or": []},
        )

        for child_task in child_tasks.values():
            assert isinstance(child_task, TaskPage)

    def test_get_tasks__with_or_filter(
        self, notion: MagicMock, get_expected_base_task_filter
    ):
        page = WithTasksMixin(TasksDatabase(notion), TEST_PAGE_DATA)
        expected_base_task_filter = get_expected_base_task_filter(TEST_PAGE_DATA["id"])
        expected_or_filter = [
            {"property": "Created Time", "date": {"on_or_before": "2022-12-25"}}
        ]
        page.base_task_filter = expected_base_task_filter
        child_tasks = page.get_tasks({"or": expected_or_filter})
        notion.databases.query.assert_called_once_with(
            database_id=TasksDatabase.id,
            filter={"and": [expected_base_task_filter], "or": expected_or_filter},
        )

    def test_all_tasks(self, notion: MagicMock, get_expected_base_task_filter):
        page = WithTasksMixin(TasksDatabase(notion), TEST_PAGE_DATA)
        expected_base_task_filter = get_expected_base_task_filter(TEST_PAGE_DATA["id"])
        page.base_task_filter = expected_base_task_filter
        page.all_tasks
        notion.databases.query.assert_called_once_with(
            database_id=TasksDatabase.id,
            filter={"and": [expected_base_task_filter], "or": []},
        )

    def test_get_current_tasks(self, notion: MagicMock, get_tasks: MagicMock):
        page = WithTasksMixin(TasksDatabase(notion), TEST_PAGE_DATA)

        expected_query_filter = {
            "and": [
                WithTasksMixin._get_filter_done(False),
                WithTasksMixin._get_filter_kanban_status_not_done(),
            ],
        }
        page.get_current_tasks()
        get_tasks.assert_called_once_with(
            query_filter=expected_query_filter,
        )

    def test_get_current_tasks__include_done(self, notion: MagicMock, get_tasks: MagicMock):
        page = WithTasksMixin(TasksDatabase(notion), TEST_PAGE_DATA)

        expected_query_filter = {
            "and": [
                WithTasksMixin._get_filter_kanban_status_not_done(),
            ],
        }
        page.get_current_tasks(include_done=True)
        get_tasks.assert_called_once_with(
            query_filter=expected_query_filter,
        )

    def test_get_current_tasks__include_kanban_done(
        self, notion: MagicMock, get_tasks: MagicMock
    ):
        page = WithTasksMixin(TasksDatabase(notion), TEST_PAGE_DATA)
        expected_query_filter = {
            "and": [
                WithTasksMixin._get_filter_done(False),
            ],
        }
        page.get_current_tasks(include_kanban_done=True)
        get_tasks.assert_called_once_with(
            query_filter=expected_query_filter,
        )

    def test_get_current_tasks__include_both_done_and_kanban_done(
        self, notion: MagicMock, get_tasks: MagicMock
    ):
        page = WithTasksMixin(TasksDatabase(notion), TEST_PAGE_DATA)
        expected_query_filter = {"and": []}
        page.get_current_tasks(include_done=True, include_kanban_done=True)
        get_tasks.assert_called_once_with(
            query_filter=expected_query_filter,
        )

    def test_get_current_tasks_with_offset(self, notion: MagicMock, get_tasks: MagicMock):
        page = WithTasksMixin(TasksDatabase(notion), TEST_PAGE_DATA)
        page.get_current_tasks_with_offset()

        _, end_date = get_start_and_end_of_day(offset_days=0)
        expected_query_filter = {
            "and": [
                WithTasksMixin._get_filter_done(False),
                WithTasksMixin._get_filter_kanban_status_not_done(),
                WithTasksMixin._get_filter_date(
                    end_date=end_date - timedelta(minutes=1)
                ),
            ],
            "or": [],
        }

        get_tasks.assert_called_once_with(
            query_filter=expected_query_filter,
        )

    def test_yesterday_tasks(self, notion: MagicMock, get_tasks: MagicMock):
        page = WithTasksMixin(TasksDatabase(notion), TEST_PAGE_DATA)
        page.yesterday_tasks

        _, end_date = get_start_and_end_of_day(offset_days=-1)
        expected_query_filter = {
            "and": [
                WithTasksMixin._get_filter_date(
                    end_date=end_date - timedelta(minutes=1)
                ),
            ],
            "or": [],
        }

        get_tasks.assert_called_once_with(
            query_filter=expected_query_filter,
        )

    def test_today_tasks(self, notion: MagicMock, get_tasks: MagicMock):
        page = WithTasksMixin(TasksDatabase(notion), TEST_PAGE_DATA)
        page.today_tasks

        _, end_date = get_start_and_end_of_day(offset_days=0)
        expected_query_filter = {
            "and": [
                WithTasksMixin._get_filter_done(False),
                WithTasksMixin._get_filter_kanban_status_not_done(),
                WithTasksMixin._get_filter_date(
                    end_date=end_date - timedelta(minutes=1)
                ),
            ],
            "or": [],
        }

        get_tasks.assert_called_once_with(
            query_filter=expected_query_filter,
        )

    def test_tomorrow_tasks(self, notion: MagicMock, get_tasks: MagicMock):
        page = WithTasksMixin(TasksDatabase(notion), TEST_PAGE_DATA)
        page.tomorrow_tasks

        _, end_date = get_start_and_end_of_day(offset_days=1)
        expected_query_filter = {
            "and": [
                WithTasksMixin._get_filter_done(False),
                WithTasksMixin._get_filter_kanban_status_not_done(),
                WithTasksMixin._get_filter_date(
                    end_date=end_date - timedelta(minutes=1)
                ),
            ],
            "or": [],
        }

        get_tasks.assert_called_once_with(
            query_filter=expected_query_filter,
        )

    def test_get_completed_tasks(self, notion: MagicMock, get_tasks: MagicMock):
        page = WithTasksMixin(TasksDatabase(notion), TEST_PAGE_DATA)
        page.get_completed_tasks()

        expected_query_filter = {
            "or": [
                WithTasksMixin._get_filter_done(True),
                WithTasksMixin._get_filter_kanban_status_done("equals"),
            ],
            "and": [],
        }

        get_tasks.assert_called_once_with(
            query_filter=expected_query_filter,
        )

    def test_task_ids(self, notion: MagicMock):
        page = WithTasksMixin(TasksDatabase(notion), TEST_PAGE_DATA)

        expected_task_ids = TEST_PAGE_DATA["properties"]["Tasks"]["relation"]
        task_ids = page.task_ids

        assert len(task_ids) == len(expected_task_ids)
        assert task_ids == [task["id"] for task in expected_task_ids]

    def test_get_filter_date(self):
        start_date, end_date = get_start_and_end_of_day()

        assert WithTasksMixin._get_filter_date() == {
            "property": "Due",
            "date": {},
        }

        assert WithTasksMixin._get_filter_date(start_date=start_date) == {
            "property": "Due",
            "date": {
                "on_or_after": to_notion_strftime(start_date)
            },
        }

        assert WithTasksMixin._get_filter_date(end_date=end_date) == {
            "property": "Due",
            "date": {
                "on_or_before": to_notion_strftime(end_date)
            },
        }

        assert WithTasksMixin._get_filter_date(start_date=start_date, end_date=end_date) == {
            "property": "Due",
            "date": {
                "on_or_after": to_notion_strftime(start_date),
                "on_or_before": to_notion_strftime(end_date),
            },
        }
        