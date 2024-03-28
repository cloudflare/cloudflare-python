# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["FailedLoginListResponse"]


class FailedLoginListResponse(BaseModel):
    expiration: Optional[int] = None

    metadata: Optional[object] = None
