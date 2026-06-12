# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ....._models import BaseModel

__all__ = ["ISPs", "ISP", "ISPIP", "ISPIPLocation"]


class ISPIPLocation(BaseModel):
    """Geographic location information.

    All fields are returned as the literal string `"REDACTED"` for callers that do not have the PII permission.
    """

    city: Optional[str] = None
    """City name. Returned as `"REDACTED"` without PII permission."""

    country_iso: Optional[str] = None
    """Country ISO code. Returned as `"REDACTED"` without PII permission."""

    state_iso: Optional[str] = None
    """State/province ISO code. Returned as `"REDACTED"` without PII permission."""

    zip: Optional[str] = None
    """ZIP/postal code. Returned as `"REDACTED"` without PII permission."""


class ISPIP(BaseModel):
    """IP address information for the ISP hop.

    Fields marked as PII-gated (`name`, `address`, `netmask`, and all `location` sub-fields) will be returned as the literal string `"REDACTED"` for callers that do not have the PII permission. `asn`, `aso`, and `version` are always returned regardless of PII access.
    """

    address: Optional[str] = None
    """IP address. Returned as `"REDACTED"` without PII permission."""

    asn: Optional[int] = None
    """Autonomous System Number."""

    aso: Optional[str] = None
    """Autonomous System Organization name."""

    location: Optional[ISPIPLocation] = None
    """Geographic location information.

    All fields are returned as the literal string `"REDACTED"` for callers that do
    not have the PII permission.
    """

    name: Optional[str] = None
    """Named IP address (reverse DNS hostname when available).

    Returned as `"REDACTED"` without PII permission.
    """

    netmask: Optional[str] = None
    """Network mask. Returned as `"REDACTED"` without PII permission."""

    version: Optional[int] = None
    """IP version (`1` for IPv4, `2` for IPv6, `0` if unknown)."""


class ISP(BaseModel):
    test_id: str
    """The test that generated this result."""

    test_result_id: str
    """The specific test result."""

    time_start: datetime
    """Timestamp of when the ISP was observed."""

    ip: Optional[ISPIP] = None
    """IP address information for the ISP hop.

    Fields marked as PII-gated (`name`, `address`, `netmask`, and all `location`
    sub-fields) will be returned as the literal string `"REDACTED"` for callers that
    do not have the PII permission. `asn`, `aso`, and `version` are always returned
    regardless of PII access.
    """


class ISPs(BaseModel):
    isps: List[ISP]
