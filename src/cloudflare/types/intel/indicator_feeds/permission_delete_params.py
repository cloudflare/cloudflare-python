# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PermissionDeleteParams"]


class PermissionDeleteParams(TypedDict, total=False):
    account_id: str
    """Identifier"""

    account_tag: str
    """The Cloudflare account tag of the account to change permissions on"""

    feed_id: int
    """The ID of the feed to add/remove permissions on"""
