# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["CustomPage"]


class CustomPage(BaseModel):
    custom_html: str
    """Custom page HTML."""

    name: str
    """Custom page name."""

    type: Literal["identity_denied", "forbidden", "login", "interstitial"]
    """Custom page type."""

    contract_version: Optional[int] = None
    """Contract version of the page's Liquid template.

    Present (>= 1) marks a sanitized template; absent or 0 marks a legacy page
    served verbatim.
    """

    uid: Optional[str] = None
    """UUID."""
