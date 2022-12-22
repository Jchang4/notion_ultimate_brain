from datetime import datetime, timedelta
from typing import Any, Dict, List, Tuple, TypeVar, Union

from dateutil import parser

JSON = Dict[str, Any]
PROPERTY_VALUE = Union[str, int, float, JSON, List[JSON], List[str]]
T = TypeVar("T")


def dict_by(items: List[T], prop: str) -> Dict[Any, T]:
    return {getattr(item, prop): item for item in items}


def nonnulls(items):
    return [item for item in items if item is not None]


def flatten(arrs):
    result = []
    for arr in arrs:
        result.extend(arr)
    return result


def to_notion_strftime(date: datetime) -> str:
    return date.isoformat()


def get_day_midnight(strftime: str = "", offset_days: int = 0) -> datetime:
    date = parser.parse(strftime) if strftime else datetime.now()
    date += timedelta(days=offset_days)
    return date.replace(hour=0, minute=0, second=0, microsecond=0)


def get_start_and_end_of_day(offset_days: int = 0) -> Tuple[datetime, datetime]:
    day = get_day_midnight(offset_days=offset_days)
    return day, day.replace(hour=23, minute=59, second=59)


def query_filter_merge(*dicts) -> JSON:
    result = {
        "and": [],
        "or": [],
    }
    for d in dicts:
        if "and" in d:
            result["and"] += d["and"]
        if "or" in d:
            result["or"] += d["or"]
    return result
