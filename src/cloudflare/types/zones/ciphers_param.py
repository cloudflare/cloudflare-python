# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CiphersParam"]


class CiphersParam(TypedDict, total=False):
    id: Required[Literal["ciphers"]]
    """ID of the zone setting."""

    value: Required[List[str]]
    """Current value of the zone setting."""
