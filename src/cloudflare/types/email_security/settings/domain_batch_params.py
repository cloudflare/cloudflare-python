# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["DomainBatchParams", "Delete", "Patch", "Post", "Put"]


class DomainBatchParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    deletes: Required[Iterable[Delete]]
    """IDs of the domains to remove protection from."""

    patches: Required[Iterable[Patch]]
    """
    Partial updates to apply — each entry carries the domain's ID and only the
    fields to change.
    """

    posts: Required[Iterable[Post]]
    """Domains to add protection for."""

    puts: Required[Iterable[Put]]
    """
    Full replacements to apply — each entry carries the domain's ID and every field
    of its new value.
    """


class Delete(TypedDict, total=False):
    id: Required[str]
    """Domain identifier."""


class Patch(TypedDict, total=False):
    id: Required[str]
    """Domain identifier."""

    allowed_delivery_modes: List[Literal["DIRECT", "BCC", "JOURNAL", "API", "RETRO_SCAN"]]
    """Delivery modes to onboard the domain through."""

    drop_dispositions: List[
        Literal[
            "MALICIOUS",
            "MALICIOUS-BEC",
            "SUSPICIOUS",
            "SPOOF",
            "SPAM",
            "BULK",
            "ENCRYPTED",
            "EXTERNAL",
            "UNKNOWN",
            "NONE",
        ]
    ]
    """Dispositions to drop instead of delivering, e.g. `["MALICIOUS", "SPAM"]`."""

    folder: Optional[Literal["AllItems", "Inbox"]]
    """The mailbox folder to scan, for API-scanning domains."""

    integration_id: Optional[str]
    """Identifier of the CASB integration that authorizes this domain.

    The integration also enables API scanning, post-delivery actions, and directory
    sync.
    """

    ip_restrictions: SequenceNotStr[str]
    """Source IP ranges mail is accepted from. Any other source is rejected."""

    lookback_hops: int
    """
    Number of hops to trace back through received headers when reconstructing the
    original message (1-20).
    """

    regions: List[Literal["GLOBAL", "AU", "DE", "IN", "US"]]
    """Regions that process messages for this domain, e.g. `["GLOBAL"]` or `["US"]`."""

    require_tls_inbound: bool
    """Require TLS on inbound connections."""

    require_tls_outbound: bool
    """Require TLS on outbound connections."""

    transport: str
    """
    The mail transport hostname for MX/Inline delivery — the MX record Cloudflare
    delivers email to (e.g. `mx.example.com`).
    """


class Post(TypedDict, total=False):
    allowed_delivery_modes: Required[List[Literal["DIRECT", "BCC", "JOURNAL", "API", "RETRO_SCAN"]]]
    """Delivery modes to onboard the domain through."""

    domain: Required[str]
    """The email domain to protect."""

    drop_dispositions: Required[
        List[
            Literal[
                "MALICIOUS",
                "MALICIOUS-BEC",
                "SUSPICIOUS",
                "SPOOF",
                "SPAM",
                "BULK",
                "ENCRYPTED",
                "EXTERNAL",
                "UNKNOWN",
                "NONE",
            ]
        ]
    ]
    """Dispositions to drop instead of delivering, e.g. `["MALICIOUS", "SPAM"]`."""

    ip_restrictions: Required[SequenceNotStr[str]]
    """Source IP ranges mail is accepted from. Any other source is rejected."""

    regions: Required[List[Literal["GLOBAL", "AU", "DE", "IN", "US"]]]
    """Regions that process messages for this domain, e.g. `["GLOBAL"]` or `["US"]`."""

    folder: Optional[Literal["AllItems", "Inbox"]]
    """The mailbox folder to scan, for API-scanning domains."""

    integration_id: Optional[str]
    """Identifier of the CASB integration that authorizes this domain.

    The integration also enables API scanning, post-delivery actions, and directory
    sync.
    """

    lookback_hops: Optional[int]
    """
    Number of hops to trace back through received headers when reconstructing the
    original message (1-20).
    """

    require_tls_inbound: Optional[bool]
    """Require TLS on inbound connections."""

    require_tls_outbound: Optional[bool]
    """Require TLS on outbound connections."""

    transport: Optional[str]
    """
    The mail transport hostname for MX/Inline delivery — the MX record Cloudflare
    delivers email to (e.g. `mx.example.com`).
    """


class Put(TypedDict, total=False):
    """Request body for replacing an email domain.

    The `domain` field is intentionally
    absent — the domain name is immutable after creation.
    """

    id: Required[str]
    """Domain identifier."""

    allowed_delivery_modes: Required[List[Literal["DIRECT", "BCC", "JOURNAL", "API", "RETRO_SCAN"]]]
    """Delivery modes to onboard the domain through."""

    drop_dispositions: Required[
        List[
            Literal[
                "MALICIOUS",
                "MALICIOUS-BEC",
                "SUSPICIOUS",
                "SPOOF",
                "SPAM",
                "BULK",
                "ENCRYPTED",
                "EXTERNAL",
                "UNKNOWN",
                "NONE",
            ]
        ]
    ]
    """Dispositions to drop instead of delivering, e.g. `["MALICIOUS", "SPAM"]`."""

    ip_restrictions: Required[SequenceNotStr[str]]
    """Source IP ranges mail is accepted from. Any other source is rejected."""

    regions: Required[List[Literal["GLOBAL", "AU", "DE", "IN", "US"]]]
    """Regions that process messages for this domain, e.g. `["GLOBAL"]` or `["US"]`."""

    folder: Optional[Literal["AllItems", "Inbox"]]
    """The mailbox folder to scan, for API-scanning domains."""

    integration_id: Optional[str]
    """Identifier of the CASB integration that authorizes this domain.

    The integration also enables API scanning, post-delivery actions, and directory
    sync.
    """

    lookback_hops: Optional[int]
    """
    Number of hops to trace back through received headers when reconstructing the
    original message (1-20).
    """

    require_tls_inbound: Optional[bool]
    """Require TLS on inbound connections."""

    require_tls_outbound: Optional[bool]
    """Require TLS on outbound connections."""

    transport: Optional[str]
    """
    The mail transport hostname for MX/Inline delivery — the MX record Cloudflare
    delivers email to (e.g. `mx.example.com`).
    """
