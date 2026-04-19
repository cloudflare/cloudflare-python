# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["JobUpdateParams"]


class JobUpdateParams(TypedDict, total=False):
    account_id: str

    name: Required[str]

    id: Required[str]
    """AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores."""

    action: Required[Literal["cancel"]]
