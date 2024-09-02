# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, Union

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["DNSRecord"]


class DNSRecord(BaseModel):
    content: Optional[str] = None
    """DNS record content."""

    name: Optional[str] = None
    """DNS record name (or @ for the zone apex)."""

    priority: Optional[float] = None
    """Required for MX, SRV and URI records.

    Unused by other record types. Records with lower priorities are preferred.
    """

    ttl: Union[float, Literal[1], None] = None
    """Time to live, in seconds, of the DNS record.

    Must be between 60 and 86400, or 1 for 'automatic'.
    """

    type: Optional[
        Literal[
            "A",
            "AAAA",
            "CNAME",
            "HTTPS",
            "TXT",
            "SRV",
            "LOC",
            "MX",
            "NS",
            "CERT",
            "DNSKEY",
            "DS",
            "NAPTR",
            "SMIMEA",
            "SSHFP",
            "SVCB",
            "TLSA",
            "URI",
        ]
    ] = None
    """DNS record type."""
