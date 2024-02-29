# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["CertificateUpdateParams"]


class CertificateUpdateParams(TypedDict, total=False):
    associated_hostnames: Required[List[str]]
    """The hostnames of the applications that will use this certificate."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    name: str
    """The name of the certificate."""
