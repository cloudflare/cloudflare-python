# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ....._models import BaseModel

__all__ = ["FlagLogsReceivedUpdateLogRetentionFlagResponse"]


class FlagLogsReceivedUpdateLogRetentionFlagResponse(BaseModel):
    flag: Optional[bool] = None
