# File generated from our OpenAPI spec by Stainless.

from typing import List, Union, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ImagesImage"]


class ImagesImage(BaseModel):
    id: Optional[str] = None
    """Image unique identifier."""

    filename: Optional[str] = None
    """Image file name."""

    meta: Optional[object] = None
    """User modifiable key-value store.

    Can be used for keeping references to another system of record for managing
    images. Metadata must not exceed 1024 bytes.
    """

    require_signed_urls: Optional[bool] = FieldInfo(alias="requireSignedURLs", default=None)
    """Indicates whether the image can be a accessed only using it's UID.

    If set to true, a signed token needs to be generated with a signing key to view
    the image.
    """

    uploaded: Optional[datetime] = None
    """When the media item was uploaded."""

    variants: Optional[List[Union[str, str, str]]] = None
    """Object specifying available variants for an image."""
