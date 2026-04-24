# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IPGetParams"]


class IPGetParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID"""

    default_virtual_network_fallback: bool
    """
    When the virtual_network_id parameter is not provided the request filter will
    default search routes that are in the default virtual network for the account.
    If this parameter is set to false, the search will include routes that do not
    have a virtual network.
    """

    virtual_network_id: str
    """UUID of the virtual network."""
