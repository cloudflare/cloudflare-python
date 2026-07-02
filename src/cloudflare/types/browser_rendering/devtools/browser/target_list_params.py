# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["TargetListParams"]


class TargetListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    live_view_url_expires_in_ms: Annotated[float, PropertyInfo(alias="liveViewUrlExpiresInMs")]
    """How long the live view URLs remain valid, in milliseconds (max 60 minutes)"""
