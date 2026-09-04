# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["URLGetParams"]


class URLGetParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    url: Required[str]
    """The URL to look up."""
