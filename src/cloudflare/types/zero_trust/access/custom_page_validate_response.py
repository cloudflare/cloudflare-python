# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["CustomPageValidateResponse", "Error", "Warning"]


class Error(BaseModel):
    """A single validation finding for a template."""

    message: str
    """Human-readable description of the finding."""

    tier: str
    """The validation tier that produced the finding (e.g. html, liquid)."""

    ref: Optional[str] = None
    """Optional pointer to the part of the template the finding refers to."""


class Warning(BaseModel):
    """A single validation finding for a template."""

    message: str
    """Human-readable description of the finding."""

    tier: str
    """The validation tier that produced the finding (e.g. html, liquid)."""

    ref: Optional[str] = None
    """Optional pointer to the part of the template the finding refers to."""


class CustomPageValidateResponse(BaseModel):
    """The result of validating a template's content."""

    errors: List[Error]
    """Blocking findings; a non-empty list means the template cannot be published."""

    page_type: Literal["identity_denied", "forbidden", "login", "interstitial"]
    """Custom page type."""

    version: int
    """The contract version the template was validated against."""

    warnings: List[Warning]
    """Advisory findings that do not block publishing."""
