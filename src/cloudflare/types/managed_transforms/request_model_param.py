# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RequestModelParam"]


class RequestModelParam(TypedDict, total=False):
    id: str
    """Human-readable identifier of the Managed Transform."""

    enabled: bool
    """When true, the Managed Transform is enabled."""
