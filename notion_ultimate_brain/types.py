from typing import Any, Dict, List, Union

JSON = Dict[str, Any]
PROPERTY_VALUE = Union[str, int, float, JSON, List[JSON], List[str]]


class WithRawPayload:
    _raw: JSON

    def __init__(self, raw: JSON, *args: Any, **kargs: Any) -> None:
        super().__init__(*args, **kargs)
        self._raw = raw
