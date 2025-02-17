# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["ImpersonationRegistryGetResponse"]


class ImpersonationRegistryGetResponse(BaseModel):
    id: int

    created_at: datetime

    is_email_regex: bool

    last_modified: datetime

    name: str

    comments: Optional[str] = None

    directory_id: Optional[int] = None

    directory_node_id: Optional[int] = None

    email: Optional[str] = None

    external_directory_node_id: Optional[str] = None

    provenance: Optional[str] = None
