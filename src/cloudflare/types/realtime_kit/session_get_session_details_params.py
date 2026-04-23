# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SessionGetSessionDetailsParams"]


class SessionGetSessionDetailsParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    app_id: Required[str]
    """The app identifier tag."""

    include_breakout_rooms: bool
    """List all breakout rooms"""
