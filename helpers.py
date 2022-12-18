import operator
from functools import reduce
from typing import Any, Callable, Dict, List, Optional, TypeVar

T = TypeVar("T")


def dict_by(items: List[T], prop: str) -> Dict[Any, T]:
    return {getattr(item, prop): item for item in items}


def assert_nonnull(item: Optional[T]) -> T:
    assert item is not None
    return item


def nonnulls(items: List[Optional[T]]) -> List[T]:
    return [item for item in items if item]


def pipe(*funcs: Callable[[Any], Any]) -> Callable[[Any], Any]:
    def _inner(x) -> Any:
        return reduce(lambda x, fn: fn(x), funcs, x)

    return _inner


def find(element, json, default: Optional[T] = None) -> T:
    props = element.split(".")
    for p in props[:-1]:
        json = json.get(p, {})
    return json.get(props[-1], default)
