from notion_client import Client

from notion_ultimate_brain.databases.tasks import TasksDatabase
from notion_ultimate_brain.notion.all import NotionPage
from notion_ultimate_brain.pages.task import TaskPage


class TestTasksDatabase:
    def test_create(self):
        raw_data = {"id": "database_id"}
        notion = Client()
        tasks = TasksDatabase(notion, raw_data)
        assert isinstance(tasks, TasksDatabase)
        assert tasks._raw == raw_data
        assert tasks.id == raw_data["id"]

    def test_default_database_id(self):
        notion = Client()
        tasks = TasksDatabase(notion)
        assert tasks._raw == {"id": TasksDatabase.database_id}
        assert tasks.id == TasksDatabase.database_id

    def test_update_id_to_pages(self):
        notion = Client()
        tasks = TasksDatabase(notion)

        assert not tasks.id_to_page

        expected_pages = {
            f"page_{i}": NotionPage(tasks, {"id": f"page_{i}"}) for i in range(5)
        }
        tasks._update_id_to_pages(list(expected_pages.values()))
        assert tasks.id_to_page

        assert len(tasks.id_to_page) == len(expected_pages)

        for page_id, actual_page in tasks.id_to_page.items():
            assert isinstance(actual_page, TaskPage)
            assert page_id in expected_pages
            expected_page = expected_pages[page_id]
            assert actual_page._raw == expected_page._raw
            assert actual_page.id == expected_page.id
