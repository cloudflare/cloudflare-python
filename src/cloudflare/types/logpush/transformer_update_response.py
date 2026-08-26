# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TransformerUpdateResponse", "AssociatedJob"]


class AssociatedJob(BaseModel):
    id: Optional[int] = None
    """The logpush job ID."""

    name: Optional[str] = None
    """The logpush job destination name."""

    object_tag: Optional[str] = None
    """The zone or account tag."""

    object_type: Optional[Literal["zone", "account"]] = None
    """Whether the job is zone-scoped or account-scoped."""


class TransformerUpdateResponse(BaseModel):
    id: Optional[int] = None
    """The transformer ID."""

    associated_jobs: Optional[List[AssociatedJob]] = None
    """Logpush jobs that reference this transformer."""

    created_at: Optional[datetime] = None
    """When the transformer was created (RFC 3339)."""

    dataset: Optional[str] = None
    """
    The dataset this transformer operates on, derived from the SQL query's FROM
    clause. Informational only. May be absent if the dataset cannot be determined
    from the query.
    """

    description: Optional[str] = None
    """Optional customer-provided description."""

    name: Optional[str] = None
    """Customer-provided name for identification."""

    updated_at: Optional[datetime] = None
    """When the transformer was last modified (RFC 3339)."""
