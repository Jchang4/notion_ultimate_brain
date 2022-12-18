from helpers import find
from notion_helpers.data_types.notion_properties.__tests__.helpers import (
    DATABASE_PROPERTY_DATA,
    PAGE_PROPERTY_DATA,
    PropertyTypes,
)
from notion_helpers.data_types.notion_properties.relation_property import (
    RelationProperty,
)


class TestRelationProperty:
    raw_relation_properties_data_from_database = DATABASE_PROPERTY_DATA[
        PropertyTypes.RELATION
    ]
    raw_relation_properties_data_from_page = PAGE_PROPERTY_DATA[PropertyTypes.RELATION]

    def test_create_from_database(self):
        for json_data in self.raw_relation_properties_data_from_database.values():
            actual = RelationProperty(json_data)
            assert actual.type == PropertyTypes.RELATION
            assert actual.value.linked_ids == []

            source = actual.value.source
            print(source)
            assert source is not None
            assert source.database_id == find("relation.database_id", json_data)
            assert source.type == find("relation.type", json_data)
            assert source.dual_property_synced_property_name == find(
                "relation.dual_property.synced_property_name", json_data
            )
            assert source.dual_property_synced_property_id == find(
                "relation.dual_property.synced_property_id", json_data
            )

    def test_create_from_page(self):
        for json_data in self.raw_relation_properties_data_from_page.values():
            actual = RelationProperty(json_data)
            assert actual.type == PropertyTypes.RELATION
            assert actual.value.source is None
            assert actual.value.linked_ids is not None
            assert sorted(actual.value.linked_ids) == sorted(
                [r["id"] for r in find("relation", json_data)]
            )
