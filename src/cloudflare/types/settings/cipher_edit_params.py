# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["CipherEditParams"]


class CipherEditParams(TypedDict, total=False):
    value: Required[List[str]]
    """Value of the zone setting."""
