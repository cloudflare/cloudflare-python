# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ImpersonationRegistryListResponse"]


class ImpersonationRegistryListResponse(BaseModel):
    """An impersonation registry entry."""

    id: Optional[str] = None
    """Impersonation registry entry identifier."""

    comments: Optional[str] = None
    """Optional note describing the entry."""

    created_at: Optional[datetime] = None

    directory_id: Optional[int] = None
    """Identifier of the directory the entry was synced from, when directory-synced."""

    directory_node_id: Optional[int] = None
    """
    Identifier of the directory node the entry was synced from, when
    directory-synced.
    """

    email: Optional[str] = None
    """Email address (or pattern) of the protected identity."""

    external_directory_node_id: Optional[str] = None
    """Deprecated. External identifier of the directory node."""

    is_email_regex: Optional[bool] = None
    """Whether `email` is a regular expression instead of a literal address."""

    last_modified: Optional[datetime] = None
    """Deprecated, use `modified_at` instead. End of life: November 1, 2026."""

    modified_at: Optional[datetime] = None

    name: Optional[str] = None
    """Display name of the protected identity."""

    provenance: Optional[
        Literal["A1S_INTERNAL", "SNOOPY-CASB_OFFICE_365", "SNOOPY-OFFICE_365", "SNOOPY-GOOGLE_DIRECTORY"]
    ] = None
    """Source the entry was created from."""
