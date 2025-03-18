# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["TimeseriesGroupResponseTTLResponse", "Serie0"]


class Serie0(BaseModel):
    gt_15m_lte_1h: List[str]

    gt_1d_lte_1w: List[str]

    gt_1h_lte_1d: List[str]

    gt_1m_lte_5m: List[str]

    gt_1w: List[str]

    gt_5m_lte_15m: List[str]

    lte_1m: List[str]


class TimeseriesGroupResponseTTLResponse(BaseModel):
    meta: object

    serie_0: Serie0
