# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ManagedTransformEditParams", "ManagedRequestHeader", "ManagedResponseHeader"]


class ManagedTransformEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """The unique ID of the zone."""

    managed_request_headers: Required[Iterable[ManagedRequestHeader]]
    """The list of Managed Request Transforms."""

    managed_response_headers: Required[Iterable[ManagedResponseHeader]]
    """The list of Managed Response Transforms."""


class ManagedRequestHeader(TypedDict, total=False):
    id: Required[str]
    """The human-readable identifier of the Managed Transform."""

    enabled: Required[bool]
    """Whether the Managed Transform is enabled."""


class ManagedResponseHeader(TypedDict, total=False):
    id: Required[str]
    """The human-readable identifier of the Managed Transform."""

    enabled: Required[bool]
    """Whether the Managed Transform is enabled."""
