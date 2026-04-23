# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CertificateCreateParams"]


class CertificateCreateParams(TypedDict, total=False):
    account_id: Required[str]

    validity_period_days: int
    """Sets the certificate validity period in days (range: 1-10,950 days / ~30 years).

    Defaults to 1,825 days (5 years). **Important**: This field is only settable
    during the certificate creation. Certificates becomes immutable after creation -
    use the `/activate` and `/deactivate` endpoints to manage certificate lifecycle.
    """
