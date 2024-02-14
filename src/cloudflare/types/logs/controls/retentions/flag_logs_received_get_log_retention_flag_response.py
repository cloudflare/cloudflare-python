# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ....._models import BaseModel

__all__ = ["FlagLogsReceivedGetLogRetentionFlagResponse"]


class FlagLogsReceivedGetLogRetentionFlagResponse(BaseModel):
    flag: Optional[bool] = None
