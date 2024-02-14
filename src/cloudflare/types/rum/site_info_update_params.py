# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SiteInfoUpdateParams"]


class SiteInfoUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    auto_install: bool
    """
    If enabled, the JavaScript snippet is automatically injected for orange-clouded
    sites.
    """

    host: str
    """The hostname to use for gray-clouded sites."""

    zone_tag: str
    """The zone identifier."""
