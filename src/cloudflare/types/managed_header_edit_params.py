# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ManagedHeaderEditParams", "ManagedRequestHeader", "ManagedResponseHeader"]


class ManagedHeaderEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    managed_request_headers: Required[Iterable[ManagedRequestHeader]]

    managed_response_headers: Required[Iterable[ManagedResponseHeader]]


class ManagedRequestHeader(TypedDict, total=False):
    id: str
    """Human-readable identifier of the Managed Transform."""

    enabled: bool
    """When true, the Managed Transform is enabled."""


class ManagedResponseHeader(TypedDict, total=False):
    id: str
    """Human-readable identifier of the Managed Transform."""

    enabled: bool
    """When true, the Managed Transform is enabled."""
