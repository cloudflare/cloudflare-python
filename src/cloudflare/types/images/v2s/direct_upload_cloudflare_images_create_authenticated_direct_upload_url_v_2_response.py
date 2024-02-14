# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["DirectUploadCloudflareImagesCreateAuthenticatedDirectUploadURLV2Response"]


class DirectUploadCloudflareImagesCreateAuthenticatedDirectUploadURLV2Response(BaseModel):
    id: Optional[str] = None
    """Image unique identifier."""

    upload_url: Optional[str] = FieldInfo(alias="uploadURL", default=None)
    """
    The URL the unauthenticated upload can be performed to using a single HTTP POST
    (multipart/form-data) request.
    """
