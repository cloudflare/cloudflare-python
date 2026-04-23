# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BrowserLaunchParams"]


class BrowserLaunchParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    keep_alive: float
    """Keep-alive time in ms (only valid when acquiring new session)."""

    lab: bool
    """Use experimental browser."""

    recording: bool
