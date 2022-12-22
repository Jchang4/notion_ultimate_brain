from typing import Any

from notion_client import Client

from .helpers import JSON


class WithRawPayloadMixin:
    _raw: JSON

    def __init__(self, raw: JSON, *args: Any, **kargs: Any) -> None:
        super().__init__(*args, **kargs)
        self._raw = raw


class WithClientMixin:
    notion: Client

    def __init__(self, notion: Client, **kargs: Any) -> None:
        super().__init__(**kargs)
        self.notion = notion
