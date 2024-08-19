# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ClientCertificateCreateParams"]


class ClientCertificateCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    csr: Required[str]
    """The Certificate Signing Request (CSR). Must be newline-encoded."""

    validity_days: Required[int]
    """
    The number of days the Client Certificate will be valid after the issued_on date
    """
