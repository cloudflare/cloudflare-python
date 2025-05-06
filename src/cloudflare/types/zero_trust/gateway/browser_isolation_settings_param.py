# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BrowserIsolationSettingsParam"]


class BrowserIsolationSettingsParam(TypedDict, total=False):
    non_identity_enabled: bool
    """Enable non-identity onramp support for Browser Isolation."""

    url_browser_isolation_enabled: bool
    """Enable Clientless Browser Isolation."""
