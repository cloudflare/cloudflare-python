# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["BinaryStorageCreateResponse"]


class BinaryStorageCreateResponse(BaseModel):
    content_type: str

    md5: str

    sha1: str

    sha256: str
