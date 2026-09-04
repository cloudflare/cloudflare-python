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

    patches: Required[Iterable[Patch]]

    posts: Required[Iterable[Post]]

    puts: Required[Iterable[Put]]


class Delete(TypedDict, total=False):
    id: Required[str]
    """Domain identifier."""


class Patch(TypedDict, total=False):
    id: Required[str]
    """Domain identifier."""

    allowed_delivery_modes: List[Literal["DIRECT", "BCC", "JOURNAL", "API", "RETRO_SCAN"]]

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

    folder: Optional[Literal["AllItems", "Inbox"]]

    integration_id: Optional[str]

    ip_restrictions: SequenceNotStr[str]

    lookback_hops: int

    regions: List[Literal["GLOBAL", "AU", "DE", "IN", "US"]]

    require_tls_inbound: bool

    require_tls_outbound: bool

    transport: str


class Post(TypedDict, total=False):
    allowed_delivery_modes: Required[List[Literal["DIRECT", "BCC", "JOURNAL", "API", "RETRO_SCAN"]]]

    domain: Required[str]

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

    ip_restrictions: Required[SequenceNotStr[str]]

    regions: Required[List[Literal["GLOBAL", "AU", "DE", "IN", "US"]]]

    folder: Optional[Literal["AllItems", "Inbox"]]

    integration_id: Optional[str]

    lookback_hops: Optional[int]

    require_tls_inbound: Optional[bool]

    require_tls_outbound: Optional[bool]

    transport: Optional[str]


class Put(TypedDict, total=False):
    """Request body for replacing an email domain.

    The `domain` field is intentionally
    absent — the domain name is immutable after creation.
    """

    id: Required[str]
    """Domain identifier."""

    allowed_delivery_modes: Required[List[Literal["DIRECT", "BCC", "JOURNAL", "API", "RETRO_SCAN"]]]

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

    ip_restrictions: Required[SequenceNotStr[str]]

    regions: Required[List[Literal["GLOBAL", "AU", "DE", "IN", "US"]]]

    folder: Optional[Literal["AllItems", "Inbox"]]

    integration_id: Optional[str]

    lookback_hops: Optional[int]

    require_tls_inbound: Optional[bool]

    require_tls_outbound: Optional[bool]

    transport: Optional[str]
