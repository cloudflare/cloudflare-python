# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PrefixEditParams", "OnDemand"]


class PrefixEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    prefix_id: Required[str]
    """Identifier"""

    on_demand: OnDemand


class OnDemand(TypedDict, total=False):
    advertised: bool
