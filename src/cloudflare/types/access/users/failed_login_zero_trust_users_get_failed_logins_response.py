# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["FailedLoginZeroTrustUsersGetFailedLoginsResponse", "FailedLoginZeroTrustUsersGetFailedLoginsResponseItem"]


class FailedLoginZeroTrustUsersGetFailedLoginsResponseItem(BaseModel):
    expiration: Optional[int] = None

    metadata: Optional[object] = None


FailedLoginZeroTrustUsersGetFailedLoginsResponse = List[FailedLoginZeroTrustUsersGetFailedLoginsResponseItem]
