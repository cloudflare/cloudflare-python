# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["EventListResponse", "Result", "ResultASNInfo", "ResultEvent", "ResultEventTag", "ResultInfo"]

class ResultASNInfo(BaseModel):
    asn: int

    country_code: str

    org_name: str

class ResultEventTag(BaseModel):
    name: str

    score: int

class ResultEvent(BaseModel):
    id: int

    confidence_score: int

    duration: int

    event_type: int

    hijack_msgs_count: int

    hijacker_asn: int

    hijacker_country: str

    is_stale: bool

    max_hijack_ts: str

    max_msg_ts: str

    min_hijack_ts: str

    on_going_count: int

    peer_asns: List[int]

    peer_ip_count: int

    prefixes: List[str]

    tags: List[ResultEventTag]

    victim_asns: List[int]

    victim_countries: List[str]

class Result(BaseModel):
    asn_info: List[ResultASNInfo]

    events: List[ResultEvent]

    total_monitors: int

class ResultInfo(BaseModel):
    count: int

    page: int

    per_page: int

    total_count: int

class EventListResponse(BaseModel):
    result: Result

    result_info: ResultInfo

    success: bool