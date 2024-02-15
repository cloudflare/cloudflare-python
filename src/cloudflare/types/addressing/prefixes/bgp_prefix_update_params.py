# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BGPPrefixUpdateParams", "OnDemand"]


class BGPPrefixUpdateParams(TypedDict, total=False):
    account_identifier: Required[str]
    """Identifier"""

    prefix_identifier: Required[str]
    """Identifier"""

    on_demand: OnDemand


class OnDemand(TypedDict, total=False):
    advertised: bool
