# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ....._models import BaseModel

__all__ = ["QuotaGetResponse"]


class QuotaGetResponse(BaseModel):
    quota: float
    """The remaining number of commands that can be initiated for an account"""

    quota_usage: float
    """The number of commands that have been initiated for an account"""

    reset_time: datetime
    """The time when the quota resets"""
