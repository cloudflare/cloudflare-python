# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["CustomPageWithoutHTML", "Warning"]


class Warning(BaseModel):
    """A single validation finding for a template."""

    message: str
    """Human-readable description of the finding."""

    tier: str
    """The validation tier that produced the finding (e.g. html, liquid)."""

    ref: Optional[str] = None
    """Optional pointer to the part of the template the finding refers to."""


class CustomPageWithoutHTML(BaseModel):
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

    warnings: Optional[List[Warning]] = None
    """Advisory validation findings returned when creating or updating a template.

    Omitted when empty.
    """
