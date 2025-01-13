# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DomainEditParams"]


class DomainEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    ip_restrictions: Required[List[str]]

    domain: Optional[str]

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

    folder: Literal["AllItems", "Inbox"]

    integration_id: Optional[str]

    lookback_hops: Optional[int]

    require_tls_inbound: bool

    require_tls_outbound: bool

    transport: str
