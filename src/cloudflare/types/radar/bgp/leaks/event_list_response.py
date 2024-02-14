# File generated from our OpenAPI spec by Stainless.

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ....._models import BaseModel
from .....types import shared

__all__ = ["EventListResponse", "AsnInfo", "Event"]


class AsnInfo(BaseModel):
    asn: int

    country_code: str

    org_name: str


class Event(BaseModel):
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


class EventListResponse(BaseModel):
    asn_info: List[AsnInfo]

    events: List[Event]
