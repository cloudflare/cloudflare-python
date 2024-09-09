# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["EntityGetParams"]


class EntityGetParams(TypedDict, total=False):
    ip: Required[str]
    """IP address."""

    format: Literal["JSON", "CSV"]
    """Format results are returned in."""
