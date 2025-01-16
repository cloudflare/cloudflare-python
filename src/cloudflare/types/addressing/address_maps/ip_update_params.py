# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IPUpdateParams"]


class IPUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier of a Cloudflare account."""

    address_map_id: Required[str]
    """Identifier of an Address Map."""

    body: Required[object]
