# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CustomCsrListResponse"]


class CustomCsrListResponse(BaseModel):
    """A custom Certificate Signing Request (CSR)."""

    id: str
    """Custom CSR identifier tag."""

    created_at: datetime
    """When the CSR was created."""

    key_type: Literal["rsa2048", "p256v1"]
    """The key algorithm used to generate the CSR."""

    account_tag: Optional[str] = None
    """Account identifier associated with this CSR."""

    common_name: Optional[str] = None
    """The common name (domain) for the CSR."""

    country: Optional[str] = None
    """Two-letter ISO 3166-1 alpha-2 country code."""

    csr: Optional[str] = None
    """The PEM-encoded Certificate Signing Request."""

    description: Optional[str] = None
    """Optional description for the CSR."""

    locality: Optional[str] = None
    """City or locality name."""

    name: Optional[str] = None
    """Human-readable name for the CSR."""

    organization: Optional[str] = None
    """Organization name."""

    organizational_unit: Optional[str] = None
    """Organizational unit name."""

    sans: Optional[List[str]] = None
    """Subject Alternative Names included in the CSR."""

    state: Optional[str] = None
    """State or province name."""
