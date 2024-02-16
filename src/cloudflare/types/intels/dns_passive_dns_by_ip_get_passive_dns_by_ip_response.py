# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from datetime import date

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["DNSPassiveDNSByIPGetPassiveDNSByIPResponse", "ReverseRecord"]


class ReverseRecord(BaseModel):
    first_seen: Optional[date] = None
    """First seen date of the DNS record during the time period."""

    hostname: Optional[object] = None
    """Hostname that the IP was observed resolving to."""

    last_seen: Optional[date] = None
    """Last seen date of the DNS record during the time period."""


class DNSPassiveDNSByIPGetPassiveDNSByIPResponse(BaseModel):
    count: Optional[float] = None
    """Total results returned based on your search parameters."""

    page: Optional[float] = None
    """Current page within paginated list of results."""

    per_page: Optional[float] = None
    """Number of results per page of results."""

    reverse_records: Optional[List[ReverseRecord]] = None
    """Reverse DNS look-ups observed during the time period."""
