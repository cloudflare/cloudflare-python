# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DirectUploadCreateResponse"]


class DirectUploadCreateResponse(BaseModel):
    id: Optional[str] = None
    """Image unique identifier."""

    upload_url: Optional[str] = FieldInfo(alias="uploadURL", default=None)
    """
    The URL the unauthenticated upload can be performed to using a single HTTP POST
    (multipart/form-data) request.
    """
