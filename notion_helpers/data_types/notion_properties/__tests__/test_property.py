from typing import Any

import pytest

from notion_helpers.data_types.notion_properties.property import Property


class DummyProperty(Property):
    def get_value(self, payload: Any):
        return payload


class TestProperty:
    raw_properties_data = {
        "Title": {"id": "title", "name": "Title", "type": "title", "title": {}}
    }

    def test_create(self):
        actual_property = DummyProperty(self.raw_properties_data["Title"])
        expected_property = self.raw_properties_data["Title"]

        assert actual_property._raw == expected_property
        assert actual_property.id == expected_property["id"]
        assert actual_property.name == expected_property["name"]
        assert actual_property.type == expected_property["type"]
        assert actual_property.value == expected_property["title"]

    def test_get_value_not_implemented(self):
        with pytest.raises(NotImplementedError):
            Property(self.raw_properties_data["Title"])
