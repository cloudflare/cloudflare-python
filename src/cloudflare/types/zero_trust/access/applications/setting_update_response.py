# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["SettingUpdateResponse"]


class SettingUpdateResponse(BaseModel):
    allow_iframe: Optional[bool] = None
    """Enables loading application content in an iFrame."""

    skip_interstitial: Optional[bool] = None
    """Enables automatic authentication through cloudflared."""
