import logging
import os
from typing import Any, Dict, List

from notion_client import Client

NOTION_TOKEN = os.environ.get("NOTION_TOKEN")


def create_client(log_level: int = logging.WARNING) -> Client:
    return Client(auth=NOTION_TOKEN, log_level=log_level)


def get_plain_text_from_title(title: List[Dict[str, Any]]) -> str:
    return " ".join([t["plain_text"] for t in title])
