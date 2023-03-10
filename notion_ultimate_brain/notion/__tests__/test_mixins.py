from unittest.mock import MagicMock

from notion_ultimate_brain.notion.__tests__.helpers import (
    TEST_DATABASE_DATA,
    notion_client_fixture,
)
from notion_ultimate_brain.notion.mixins import WithClientMixin, WithRawPayloadMixin


class TestWithRawPayloadMixin:
    def test_create(self):
        mixin = WithRawPayloadMixin(TEST_DATABASE_DATA)
        assert mixin._raw is not None
        assert mixin._raw == TEST_DATABASE_DATA


class TestWithClientMixin:
    def test_create(self, notion: MagicMock):
        mixin = WithClientMixin(notion)
        assert mixin.notion is not None
        assert mixin.notion == notion


class TestWithMultipleMixins:
    class DummyMixins(WithClientMixin, WithRawPayloadMixin):
        pass

    def test_create(self, notion: MagicMock):
        mixin = self.DummyMixins(notion=notion, raw=TEST_DATABASE_DATA)
        assert mixin.notion is not None
        assert mixin._raw is not None
        assert mixin.notion == notion
        assert mixin._raw == TEST_DATABASE_DATA
