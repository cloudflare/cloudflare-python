# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["CustomNameserver", "DNSRecord"]


class DNSRecord(BaseModel):
    type: Optional[Literal["A", "AAAA"]] = None
    """DNS record type."""

    value: Optional[str] = None
    """DNS record contents (an IPv4 or IPv6 address)."""


class CustomNameserver(BaseModel):
    dns_records: List[DNSRecord]
    """A and AAAA records associated with the nameserver."""

    ns_name: str
    """The FQDN of the name server."""

    status: Literal["moved", "pending", "verified"]
    """Verification status of the nameserver."""

    zone_tag: str
    """Identifier"""

    ns_set: Optional[float] = None
    """The number of the set that this name server belongs to."""
