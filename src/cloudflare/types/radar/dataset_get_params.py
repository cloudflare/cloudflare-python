# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["DatasetGetParams"]


class DatasetGetParams(TypedDict, total=False):
    date: Optional[str]
    """Filter dataset alias by date"""
