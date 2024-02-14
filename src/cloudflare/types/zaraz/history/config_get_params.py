# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ConfigGetParams"]


class ConfigGetParams(TypedDict, total=False):
    ids: Required[Iterable[int]]
    """Comma separated list of Zaraz configuration IDs"""
