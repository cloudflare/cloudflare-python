# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TURNCreateParams"]


class TURNCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    name: str
    """A short description of a TURN key, not shown to end users."""
