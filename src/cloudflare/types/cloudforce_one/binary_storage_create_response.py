# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BinaryStorageCreateResponse"]


class BinaryStorageCreateResponse(BaseModel):
    account_ids: List[str] = FieldInfo(alias="accountIds")

    content_type: str

    filenames: List[str]

    first_seen: float

    is_private: bool

    md5: str

    sha1: str

    sha256: str
