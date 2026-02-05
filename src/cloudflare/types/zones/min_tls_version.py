# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MinTLSVersion"]


class MinTLSVersion(BaseModel):
    """Only accepts HTTPS requests that use at least the TLS protocol version specified.

    For example, if TLS 1.1 is selected, TLS 1.0 connections will be rejected, while 1.1, 1.2, and 1.3 (if enabled) will be permitted.
    """

    id: Literal["min_tls_version"]
    """ID of the zone setting."""

    value: Literal["1.0", "1.1", "1.2", "1.3"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""
