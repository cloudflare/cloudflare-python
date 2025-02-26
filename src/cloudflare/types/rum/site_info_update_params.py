# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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

    enabled: bool
    """Enables or disables RUM.

    This option can be used only when auto_install is set to true.
    """

    host: str
    """The hostname to use for gray-clouded sites."""

    lite: bool
    """
    If enabled, the JavaScript snippet will not be injected for visitors from the
    EU.
    """

    zone_tag: str
    """The zone identifier."""
