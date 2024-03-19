# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FlagCreateParams"]


class FlagCreateParams(TypedDict, total=False):
    flag: Required[bool]
    """The log retention flag for Logpull API."""
