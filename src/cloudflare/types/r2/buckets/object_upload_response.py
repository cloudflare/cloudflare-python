# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ObjectUploadResponse"]


class ObjectUploadResponse(BaseModel):
    """Result of a successful object upload."""

    etag: Optional[str] = None
    """The entity tag for the uploaded object."""

    key: Optional[str] = None
    """The key (name) of the uploaded object."""

    size: Optional[str] = None
    """The size of the uploaded object in bytes (as a string)."""

    storage_class: Optional[Literal["Standard", "InfrequentAccess"]] = None
    """Storage class for newly uploaded objects, unless specified otherwise."""

    uploaded: Optional[datetime] = None
    """The date and time the object was uploaded."""

    version: Optional[str] = None
    """The version UUID of the uploaded object."""
