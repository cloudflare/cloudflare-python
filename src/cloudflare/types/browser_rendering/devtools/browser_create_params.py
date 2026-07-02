# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["BrowserCreateParams"]


class BrowserCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    keep_alive: float
    """Keep-alive time in milliseconds."""

    lab: bool
    """Use experimental browser."""

    live_view_url_expires_in_ms: Annotated[float, PropertyInfo(alias="liveViewUrlExpiresInMs")]
    """How long the live view URL remains valid, in milliseconds (max 60 minutes).

    Only used when targets is true.
    """

    recording: bool

    targets: bool
    """Include browser targets in response."""
