# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SAMLCertificateListParams"]


class SAMLCertificateListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    id: str
    """Filter by SAML certificate set UID. Accepts a comma-separated list of UIDs."""

    page: int
    """Page number of paginated results."""

    per_page: int
    """Maximum number of results per page."""
