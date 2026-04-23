# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IPProfileListParams"]


class IPProfileListParams(TypedDict, total=False):
    account_id: Required[str]

    per_page: int
    """The number of IP profiles to return per page."""
