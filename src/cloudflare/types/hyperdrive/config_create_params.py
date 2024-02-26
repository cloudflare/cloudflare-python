# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConfigCreateParams", "Origin"]


class ConfigCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    origin: Required[Origin]


class Origin(TypedDict, total=False):
    password: Required[str]
    """The password required to access your origin database.

    This value is write-only and never returned by the API.
    """
