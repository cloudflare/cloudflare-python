# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SettingUpdateParams"]


class SettingUpdateParams(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    allow_iframe: bool
    """Enables loading application content in an iFrame."""

    skip_interstitial: bool
    """Enables automatic authentication through cloudflared."""
