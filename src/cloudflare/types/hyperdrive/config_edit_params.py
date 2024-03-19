# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConfigEditParams", "Origin"]


class ConfigEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    origin: Origin


class Origin(TypedDict, total=False):
    password: Required[str]
    """The password required to access your origin database.

    This value is write-only and never returned by the API.
    """
