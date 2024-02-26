# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CallCreateParams"]


class CallCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    name: str
    """A short description of Calls app, not shown to end users."""
