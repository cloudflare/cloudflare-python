# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .watermark import Watermark

__all__ = ["DirectUploadCreateResponse"]


class DirectUploadCreateResponse(BaseModel):
    scheduled_deletion: Optional[datetime] = FieldInfo(alias="scheduledDeletion", default=None)
    """Indicates the date and time at which the video will be deleted.

    Omit the field to indicate no change, or include with a `null` value to remove
    an existing scheduled deletion. If specified, must be at least 30 days from
    upload time.
    """

    uid: Optional[str] = None
    """A Cloudflare-generated unique identifier for a media item."""

    upload_url: Optional[str] = FieldInfo(alias="uploadURL", default=None)
    """
    The URL an unauthenticated upload can use for a single
    `HTTP POST multipart/form-data` request.
    """

    watermark: Optional[Watermark] = None
