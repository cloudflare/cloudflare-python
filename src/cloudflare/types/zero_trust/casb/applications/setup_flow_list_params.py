# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SetupFlowListParams"]


class SetupFlowListParams(TypedDict, total=False):
    account_id: Required[str]

    auth_method: str
    """Filter by auth method slug. Get available slugs from GET /v2/applications."""

    environment: Literal["fedramp", "standard"]
    """Filter by environment."""
