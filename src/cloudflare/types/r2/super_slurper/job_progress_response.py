# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["JobProgressResponse"]


class JobProgressResponse(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    failed_objects: Optional[int] = FieldInfo(alias="failedObjects", default=None)

    objects: Optional[int] = None

    skipped_objects: Optional[int] = FieldInfo(alias="skippedObjects", default=None)

    status: Optional[Literal["running", "paused", "aborted", "completed"]] = None

    transferred_objects: Optional[int] = FieldInfo(alias="transferredObjects", default=None)
