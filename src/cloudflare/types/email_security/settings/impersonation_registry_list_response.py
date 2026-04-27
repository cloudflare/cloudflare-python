# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ImpersonationRegistryListResponse"]


class ImpersonationRegistryListResponse(BaseModel):
    """An impersonation registry entry"""

    id: Optional[str] = None
    """Impersonation registry entry identifier"""

    comments: Optional[str] = None

    created_at: Optional[datetime] = None

    directory_id: Optional[int] = None

    directory_node_id: Optional[int] = None

    email: Optional[str] = None

    external_directory_node_id: Optional[str] = None

    is_email_regex: Optional[bool] = None

    last_modified: Optional[datetime] = None
    """Deprecated, use `modified_at` instead. End of life: November 1, 2026."""

    modified_at: Optional[datetime] = None

    name: Optional[str] = None

    provenance: Optional[
        Literal["A1S_INTERNAL", "SNOOPY-CASB_OFFICE_365", "SNOOPY-OFFICE_365", "SNOOPY-GOOGLE_DIRECTORY"]
    ] = None
