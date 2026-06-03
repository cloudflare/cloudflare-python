# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CsamScannerEditParams", "Value"]


class CsamScannerEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier for the zone."""

    id: Literal["csam_scanner"]
    """The feature identifier."""

    value: Value
    """Writable CSAM Scanner feature configuration values."""


class Value(TypedDict, total=False):
    """Writable CSAM Scanner feature configuration values."""

    email: str
    """Notification email address for CSAM scan results.

    When changed, email verification is triggered automatically.
    """

    enabled: bool
    """Whether CSAM scanning is enabled for this zone."""

    resend_email: bool
    """
    Set to true to trigger re-sending the email verification. Write-only; never
    appears in responses (omitted when false).
    """

    sources: Dict[str, bool]
    """Map of scanning sources and their enabled state."""
