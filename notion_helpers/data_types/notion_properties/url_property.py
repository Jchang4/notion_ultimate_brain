from typing import Dict, Union
from urllib.parse import urlparse

from notion_helpers.data_types.notion_properties.property import Property


class UrlProperty(Property):
    value: str

    def get_value(self, payload: Union[Dict, str]) -> str:
        return "" if isinstance(payload, dict) else payload

    def __repr__(self) -> str:
        return super().__repr__(f"domain={self.domain}")

    @property
    def domain(self) -> str:
        return urlparse(self.value).netloc
