# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["BrowserIsolationSettings"]


class BrowserIsolationSettings(BaseModel):
    non_identity_enabled: Optional[bool] = None
    """Enable non-identity onramp support for Browser Isolation."""

    url_browser_isolation_enabled: Optional[bool] = None
    """Enable Clientless Browser Isolation."""
