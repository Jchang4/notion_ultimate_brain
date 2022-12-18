from notion_helpers.data_types.__tests__.page_data import PAGE_DATA
from notion_helpers.data_types.notion_page import Page
from notion_helpers.data_types.notion_properties.__tests__.helpers import (
    PAGE_PROPERTY_DATA,
    PropertyTypes,
)
from notion_helpers.helpers import get_plain_text_from_title


class TestPage:
    def test_create(self):
        for expected_page in PAGE_DATA:
            page = Page(expected_page)
            assert page._raw == expected_page
            assert page.id == expected_page["id"]
            assert page.title is not None
            assert page.title != ""
            assert page.title == get_plain_text_from_title(
                expected_page["properties"]["Title"]["title"]
            )

    def test_get_title(self):
        for page in PAGE_DATA:
            assert Page.get_title(page) == get_plain_text_from_title(
                page["properties"]["Title"]["title"]
            )
