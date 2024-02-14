# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = [
    "ManagedHeaderManagedTransformsUpdateStatusOfManagedTransformsParams",
    "ManagedRequestHeader",
    "ManagedResponseHeader",
]


class ManagedHeaderManagedTransformsUpdateStatusOfManagedTransformsParams(TypedDict, total=False):
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
