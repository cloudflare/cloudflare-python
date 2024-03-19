# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["FailedLoginListResponse", "FailedLoginListResponseItem"]


class FailedLoginListResponseItem(BaseModel):
    expiration: Optional[int] = None

    metadata: Optional[object] = None


FailedLoginListResponse = List[FailedLoginListResponseItem]
