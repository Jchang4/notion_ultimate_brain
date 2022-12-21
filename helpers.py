from datetime import datetime, timedelta
from functools import reduce
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, TypeVar

from dateutil import parser

T = TypeVar("T")


def first(items: Any):
    if not items:
        return None
    if not isinstance(items, Sequence):
        items = list(items)
    return items[0]


def firstx(items: Any):
    item = first(items)
    assert item is not None
    return item


def flatten(arrs):
    result = []
    for arr in arrs:
        result.extend(arr)
    return result


def dict_by(items: List[T], prop: str) -> Dict[Any, T]:
    return {getattr(item, prop): item for item in items}


def assert_nonnull(item: Optional[T], message: str = "") -> T:
    assert item is not None, message
    return item


def nonnulls(items):
    return [item for item in items if item is not None]


def pipe(*funcs: Callable[[Any], Any]) -> Callable[[Any], Any]:
    def _inner(x) -> Any:
        return reduce(lambda x, fn: fn(x), funcs, x)

    return _inner


def find(element, json, default: Optional[T] = None) -> T:
    props = element.split(".")
    for p in props[:-1]:
        json = json.get(p, {})
    return json.get(props[-1], default)


def get_day_midnight(strftime: str = "", offset_days: int = 0) -> datetime:
    date = parser.parse(strftime) if strftime else datetime.now()
    date += timedelta(days=offset_days)
    return date.replace(hour=0, minute=0, second=0, microsecond=0)


def get_start_and_end_of_day(offset_days: int = 0) -> Tuple[datetime, datetime]:
    day = get_day_midnight(offset_days=offset_days)
    return day, day + timedelta(days=1)
