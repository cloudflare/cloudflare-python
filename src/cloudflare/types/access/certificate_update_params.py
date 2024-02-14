# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["CertificateUpdateParams"]


class CertificateUpdateParams(TypedDict, total=False):
    account_or_zone: Required[str]

    account_or_zone_id: Required[str]
    """Identifier"""

    associated_hostnames: Required[List[str]]
    """The hostnames of the applications that will use this certificate."""

    name: str
    """The name of the certificate."""
