# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["SilenceUpdateParams", "Body"]


class SilenceUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """The account id"""

    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    id: str
    """Silence ID"""

    end_time: str
    """When the silence ends."""

    start_time: str
    """When the silence starts."""
