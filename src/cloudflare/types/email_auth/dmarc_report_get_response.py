# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "DMARCReportGetResponse",
    "ApprovedSource",
    "Records",
    "RecordsBimiRecord",
    "RecordsCnamedkimRecord",
    "RecordsCnamedmarcRecord",
    "RecordsCnamespfRecord",
    "RecordsDKIMRecord",
    "RecordsDMARCRecord",
    "RecordsResolvedDMARCRecord",
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

    resolved: Optional[List[str]] = None
    """
    For a CNAME record, the TXT content(s) found by following the CNAME chain to its
    target. An empty array means the chain was resolved but nothing usable was found
    there; omitted/null means resolution was not attempted for this record (always
    the case for non-CNAME entries). A CNAME chain that terminates in more than one
    TXT value at the target yields multiple entries. Populated on entries in
    cname_dmarc_records, cname_spf_records, and cname_dkim_records.
    """

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

    resolved: Optional[List[str]] = None
    """
    For a CNAME record, the TXT content(s) found by following the CNAME chain to its
    target. An empty array means the chain was resolved but nothing usable was found
    there; omitted/null means resolution was not attempted for this record (always
    the case for non-CNAME entries). A CNAME chain that terminates in more than one
    TXT value at the target yields multiple entries. Populated on entries in
    cname_dmarc_records, cname_spf_records, and cname_dkim_records.
    """

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

    resolved: Optional[List[str]] = None
    """
    For a CNAME record, the TXT content(s) found by following the CNAME chain to its
    target. An empty array means the chain was resolved but nothing usable was found
    there; omitted/null means resolution was not attempted for this record (always
    the case for non-CNAME entries). A CNAME chain that terminates in more than one
    TXT value at the target yields multiple entries. Populated on entries in
    cname_dmarc_records, cname_spf_records, and cname_dkim_records.
    """

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

    resolved: Optional[List[str]] = None
    """
    For a CNAME record, the TXT content(s) found by following the CNAME chain to its
    target. An empty array means the chain was resolved but nothing usable was found
    there; omitted/null means resolution was not attempted for this record (always
    the case for non-CNAME entries). A CNAME chain that terminates in more than one
    TXT value at the target yields multiple entries. Populated on entries in
    cname_dmarc_records, cname_spf_records, and cname_dkim_records.
    """

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

    resolved: Optional[List[str]] = None
    """
    For a CNAME record, the TXT content(s) found by following the CNAME chain to its
    target. An empty array means the chain was resolved but nothing usable was found
    there; omitted/null means resolution was not attempted for this record (always
    the case for non-CNAME entries). A CNAME chain that terminates in more than one
    TXT value at the target yields multiple entries. Populated on entries in
    cname_dmarc_records, cname_spf_records, and cname_dkim_records.
    """

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

    resolved: Optional[List[str]] = None
    """
    For a CNAME record, the TXT content(s) found by following the CNAME chain to its
    target. An empty array means the chain was resolved but nothing usable was found
    there; omitted/null means resolution was not attempted for this record (always
    the case for non-CNAME entries). A CNAME chain that terminates in more than one
    TXT value at the target yields multiple entries. Populated on entries in
    cname_dmarc_records, cname_spf_records, and cname_dkim_records.
    """

    ttl: Optional[int] = None
    """Time to live in seconds"""

    type: Optional[str] = None
    """Record type"""


class RecordsResolvedDMARCRecord(BaseModel):
    """A DMARC TXT record that a recursive lookup of _dmarc.{zone} returned.

    Such a record usually lives in another zone outside this account's control, so this schema omits the DNS record ID. The API therefore treats such a record as read-only.
    """

    content: Optional[str] = None
    """The TXT record value. The API joins all character-strings into a single string."""

    name: Optional[str] = None
    """The name the API queried."""


class RecordsSPFRecord(BaseModel):
    """Summary of a single DNS record"""

    id: Optional[str] = None
    """DNS record ID"""

    content: Optional[str] = None
    """Record content"""

    name: Optional[str] = None
    """DNS record name"""

    resolved: Optional[List[str]] = None
    """
    For a CNAME record, the TXT content(s) found by following the CNAME chain to its
    target. An empty array means the chain was resolved but nothing usable was found
    there; omitted/null means resolution was not attempted for this record (always
    the case for non-CNAME entries). A CNAME chain that terminates in more than one
    TXT value at the target yields multiple entries. Populated on entries in
    cname_dmarc_records, cname_spf_records, and cname_dkim_records.
    """

    ttl: Optional[int] = None
    """Time to live in seconds"""

    type: Optional[str] = None
    """Record type"""


class Records(BaseModel):
    """Live DNS records for the zone, grouped by type"""

    bimi_records: Optional[List[RecordsBimiRecord]] = None
    """BIMI TXT records"""

    cname_dkim_records: Optional[List[RecordsCnamedkimRecord]] = None
    """CNAME records for DKIM selectors.

    Each selector is resolved independently; when a selector's CNAME resolves to a
    DKIM TXT record, the API returns that record's content in the `resolved` field
    of the corresponding entry.
    """

    cname_dmarc_records: Optional[List[RecordsCnamedmarcRecord]] = None
    """CNAME records at \\__dmarc.

    When such a CNAME resolves to a DMARC TXT record, the API returns that record's
    content in the `resolved` field of the corresponding entry.
    """

    cname_spf_records: Optional[List[RecordsCnamespfRecord]] = None
    """CNAME records at the zone apex.

    When such a CNAME resolves to an SPF TXT record, the API returns that record's
    content in the `resolved` field of the corresponding entry.
    """

    dkim_records: Optional[List[RecordsDKIMRecord]] = None
    """DKIM TXT records"""

    dmarc_records: Optional[List[RecordsDMARCRecord]] = None
    """DMARC TXT records"""

    resolved_dmarc_records: Optional[List[RecordsResolvedDMARCRecord]] = None
    """DMARC records that a recursive lookup of \\__dmarc.{zone} returned.

    The API populates this only when the zone lacks a DMARC TXT record of its own,
    which usually means a CNAME delegates DMARC to another zone.
    """

    spf_records: Optional[List[RecordsSPFRecord]] = None
    """SPF TXT records"""


class DMARCReportGetResponse(BaseModel):
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
        Literal[
            "missing-dmarc-report",
            "multiple-dmarc-reports",
            "missing-dmarc-rua",
            "cname-on-dmarc-record",
            "unauthorized-reporting-domain",
        ]
    ] = None
    """DMARC configuration status.

    The API omits this field when DMARC is correctly configured. If the zone lacks a
    DMARC TXT record of its own, the API resolves \\__dmarc.{zone} recursively and
    evaluates whatever that lookup returns. A CNAME at \\__dmarc.{zone} that points to
    a valid DMARC record is therefore healthy; the cname-on-dmarc-record value means
    the CNAME resolves to no DMARC record at all.
    """

    tag: Optional[str] = None
    """Use `zone_id` instead"""

    zone_id: Optional[str] = None
    """Zone identifier"""
