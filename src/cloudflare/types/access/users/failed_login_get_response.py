# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["FailedLoginGetResponse", "FailedLoginGetResponseItem"]


class FailedLoginGetResponseItem(BaseModel):
    expiration: Optional[int] = None

    metadata: Optional[object] = None


FailedLoginGetResponse = List[FailedLoginGetResponseItem]
