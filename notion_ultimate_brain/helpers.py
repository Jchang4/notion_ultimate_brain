from datetime import datetime, timedelta
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, TypeVar

from dateutil import parser

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
    return day, day + timedelta(days=1)
