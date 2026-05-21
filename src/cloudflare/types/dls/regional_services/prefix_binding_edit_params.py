# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PrefixBindingEditParams"]


class PrefixBindingEditParams(TypedDict, total=False):
    account_id: Required[int]

    region_key: Required[str]
    """New region key to assign (e.g., "us", "eu", "cfcanary")."""
