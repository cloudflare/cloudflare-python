# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing_extensions import Literal

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["SecurityHeaders", "Value", "ValueStrictTransportSecurity"]

class ValueStrictTransportSecurity(BaseModel):
    enabled: Optional[bool] = None
    """Whether or not strict transport security is enabled."""

    include_subdomains: Optional[bool] = None
    """Include all subdomains for strict transport security."""

    max_age: Optional[float] = None
    """Max age in seconds of the strict transport security."""

    nosniff: Optional[bool] = None
    """Whether or not to include 'X-Content-Type-Options: nosniff' header."""

    preload: Optional[bool] = None
    """Enable automatic preload of the HSTS configuration."""

class Value(BaseModel):
    strict_transport_security: Optional[ValueStrictTransportSecurity] = None
    """Strict Transport Security."""

class SecurityHeaders(BaseModel):
    id: Literal["security_header"]
    """ID of the zone's security header."""

    value: Value
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""