# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "DMARCReportEditResponse",
    "ApprovedSource",
    "Records",
    "RecordsBimiRecord",
    "RecordsCnamedkimRecord",
    "RecordsCnamedmarcRecord",
    "RecordsCnamespfRecord",
    "RecordsDKIMRecord",
    "RecordsDMARCRecord",
    "RecordsSPFRecord",
]


class ApprovedSource(BaseModel):
    """A single approved sending source"""

    created: Optional[datetime] = None
    """Deprecated, use created_at"""

    created_at: Optional[datetime] = None
    """Creation timestamp"""

    domain: Optional[str] = None
    """The source domain"""

    ips: Optional[List[str]] = None
    """Resolved IP addresses from SPF"""

    modified: Optional[datetime] = None
    """Deprecated, use modified_at"""

    modified_at: Optional[datetime] = None
    """Last modification timestamp"""

    name: Optional[str] = None
    """Source name (typically same as domain)"""

    slug: Optional[str] = None
    """URL-friendly identifier"""

    tag: Optional[str] = None
    """Source UUID"""


class RecordsBimiRecord(BaseModel):
    """Summary of a single DNS record"""

    id: Optional[str] = None
    """DNS record ID"""

    content: Optional[str] = None
    """Record content"""

    name: Optional[str] = None
    """DNS record name"""

    ttl: Optional[int] = None
    """Time to live in seconds"""

    type: Optional[str] = None
    """Record type"""


class RecordsCnamedkimRecord(BaseModel):
    """Summary of a single DNS record"""

    id: Optional[str] = None
    """DNS record ID"""

    content: Optional[str] = None
    """Record content"""

    name: Optional[str] = None
    """DNS record name"""

    ttl: Optional[int] = None
    """Time to live in seconds"""

    type: Optional[str] = None
    """Record type"""


class RecordsCnamedmarcRecord(BaseModel):
    """Summary of a single DNS record"""

    id: Optional[str] = None
    """DNS record ID"""

    content: Optional[str] = None
    """Record content"""

    name: Optional[str] = None
    """DNS record name"""

    ttl: Optional[int] = None
    """Time to live in seconds"""

    type: Optional[str] = None
    """Record type"""


class RecordsCnamespfRecord(BaseModel):
    """Summary of a single DNS record"""

    id: Optional[str] = None
    """DNS record ID"""

    content: Optional[str] = None
    """Record content"""

    name: Optional[str] = None
    """DNS record name"""

    ttl: Optional[int] = None
    """Time to live in seconds"""

    type: Optional[str] = None
    """Record type"""


class RecordsDKIMRecord(BaseModel):
    """Summary of a single DNS record"""

    id: Optional[str] = None
    """DNS record ID"""

    content: Optional[str] = None
    """Record content"""

    name: Optional[str] = None
    """DNS record name"""

    ttl: Optional[int] = None
    """Time to live in seconds"""

    type: Optional[str] = None
    """Record type"""


class RecordsDMARCRecord(BaseModel):
    """Summary of a single DNS record"""

    id: Optional[str] = None
    """DNS record ID"""

    content: Optional[str] = None
    """Record content"""

    name: Optional[str] = None
    """DNS record name"""

    ttl: Optional[int] = None
    """Time to live in seconds"""

    type: Optional[str] = None
    """Record type"""


class RecordsSPFRecord(BaseModel):
    """Summary of a single DNS record"""

    id: Optional[str] = None
    """DNS record ID"""

    content: Optional[str] = None
    """Record content"""

    name: Optional[str] = None
    """DNS record name"""

    ttl: Optional[int] = None
    """Time to live in seconds"""

    type: Optional[str] = None
    """Record type"""


class Records(BaseModel):
    """Live DNS records for the zone, grouped by type"""

    bimi_records: Optional[List[RecordsBimiRecord]] = None
    """BIMI TXT records"""

    cname_dkim_records: Optional[List[RecordsCnamedkimRecord]] = None
    """CNAME records for DKIM"""

    cname_dmarc_records: Optional[List[RecordsCnamedmarcRecord]] = None
    """CNAME records at \\__dmarc (problematic)"""

    cname_spf_records: Optional[List[RecordsCnamespfRecord]] = None
    """CNAME records for SPF"""

    dkim_records: Optional[List[RecordsDKIMRecord]] = None
    """DKIM TXT records"""

    dmarc_records: Optional[List[RecordsDMARCRecord]] = None
    """DMARC TXT records"""

    spf_records: Optional[List[RecordsSPFRecord]] = None
    """SPF TXT records"""


class DMARCReportEditResponse(BaseModel):
    """Response for GET/PATCH /dmarc-reports"""

    approved_sources: Optional[List[ApprovedSource]] = None
    """List of approved sending sources (omitted when empty)"""

    created: Optional[datetime] = None
    """Deprecated, use created_at"""

    created_at: Optional[datetime] = None
    """Creation timestamp"""

    enabled: Optional[bool] = None
    """Whether DMARC reports are enabled"""

    modified: Optional[datetime] = None
    """Deprecated, use modified_at"""

    modified_at: Optional[datetime] = None
    """Last modification timestamp"""

    records: Optional[Records] = None
    """Live DNS records for the zone, grouped by type"""

    rua_prefix: Optional[str] = None
    """Prefix for DMARC RUA addresses (32-char hex string)"""

    skip_wizard: Optional[bool] = None
    """Whether to skip the setup wizard"""

    status: Optional[
        Literal["missing-dmarc-report", "multiple-dmarc-reports", "missing-dmarc-rua", "cname-on-dmarc-record"]
    ] = None
    """DMARC configuration status"""

    tag: Optional[str] = None
    """Use `zone_id` instead"""

    zone_id: Optional[str] = None
    """Zone identifier"""
