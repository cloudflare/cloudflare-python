# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["BillingUsageHistoryResponse", "History"]


class History(BaseModel):
    id: str

    aggregated_value: float

    end_time: float

    start_time: float


class BillingUsageHistoryResponse(BaseModel):
    history: List[History]
