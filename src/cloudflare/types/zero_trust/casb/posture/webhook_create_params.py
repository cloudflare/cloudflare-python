# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WebhookCreateParams", "Header"]


class WebhookCreateParams(TypedDict, total=False):
    account_id: Required[str]

    authentication_type: Required[Literal["Basic Auth", "None", "Bearer Auth", "Static Headers", "HMAC-Signing"]]
    """Type of authentication used for the webhook."""

    destination_url: Required[str]
    """Target URL for the webhook configuration. Where resulting data will be sent."""

    label: Required[str]
    """Account-specified display label for the webhook configuration."""

    headers: Iterable[Header]
    """List of custom headers to include in webhook requests."""

    signing_secret: str
    """Secret key used for HMAC signing when authentication_type is "HMAC-Signing"."""


class Header(TypedDict, total=False):
    """A header to include in webhook requests.

    On Create/Evaluate, both key and value are required. On Update, omitting value means "keep existing value".
    """

    key: Required[str]
    """Header key name."""

    value: Optional[str]
    """Header value.

    Required on Create and Evaluate. On Update, omit or set to null to keep existing
    value.
    """
