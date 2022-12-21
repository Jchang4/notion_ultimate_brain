from typing import Any, Dict, List


def get_plain_text_from_title(title: List[Dict[str, Any]]) -> str:
    return " ".join([t["plain_text"] for t in title])
