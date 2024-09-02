# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["EventListResponse", "Result", "ResultASNInfo", "ResultEvent", "ResultInfo"]


class ResultASNInfo(BaseModel):
    asn: int

    country_code: str

    org_name: str


class ResultEvent(BaseModel):
    id: int

    countries: List[str]

    detected_ts: str

    finished: bool

    leak_asn: int

    leak_count: int

    leak_seg: List[int]

    leak_type: int

    max_ts: str

    min_ts: str

    origin_count: int

    peer_count: int

    prefix_count: int


class Result(BaseModel):
    asn_info: List[ResultASNInfo]

    events: List[ResultEvent]


class ResultInfo(BaseModel):
    count: int

    page: int

    per_page: int

    total_count: int


class EventListResponse(BaseModel):
    result: Result

    result_info: ResultInfo

    success: bool
