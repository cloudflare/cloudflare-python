# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InspectGetParams"]


class InspectGetParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    id: Required[str]
    """DNS record ID (rec_tag) to inspect"""
