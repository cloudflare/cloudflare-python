# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CertificatePackListParams"]


class CertificatePackListParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    deploy: Literal["staging", "production"]
    """Specify the deployment environment for the certificate packs."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of certificate packs per page."""

    status: Literal["all"]
    """Include Certificate Packs of all statuses, not just active ones."""
