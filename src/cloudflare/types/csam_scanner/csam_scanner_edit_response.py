# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CsamScannerEditResponse", "Value"]


class Value(BaseModel):
    """The CSAM Scanner feature configuration values.

    Contains the
    notification email and scanning enablement settings.
    """

    email: Optional[str] = None
    """Notification email address for CSAM scan results.

    Masked in responses unless explicitly unmasked via admin endpoint.
    """

    email_state: Optional[Literal["valid", "pending", "unverified"]] = None
    """Current verification state of the notification email."""

    enabled: Optional[bool] = None
    """Whether CSAM scanning is enabled for this zone."""

    sources: Optional[Dict[str, bool]] = None
    """Map of scanning sources and their enabled state."""

    zone_plan: Optional[str] = None
    """The zone's plan level."""


class CsamScannerEditResponse(BaseModel):
    """CSAM Scanner configuration for a zone."""

    id: Optional[Literal["csam_scanner"]] = None
    """The feature identifier."""

    editable: Optional[bool] = None
    """Whether the feature state can be changed.

    When false, the zone or account may be locked by Trust & Safety.
    """

    modified_on: Optional[datetime] = None
    """When the setting was last modified.

    Currently always null as the server does not populate this field.
    """

    value: Optional[Value] = None
    """The CSAM Scanner feature configuration values.

    Contains the notification email and scanning enablement settings.
    """
