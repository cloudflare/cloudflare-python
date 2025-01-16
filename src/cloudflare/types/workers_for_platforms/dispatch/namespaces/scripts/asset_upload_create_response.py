# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ......_models import BaseModel

__all__ = ["AssetUploadCreateResponse"]


class AssetUploadCreateResponse(BaseModel):
    buckets: Optional[List[List[str]]] = None
    """The requests to make to upload assets."""

    jwt: Optional[str] = None
    """A JWT to use as authentication for uploading assets."""
