# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel

__all__ = ["EventListResponse", "ASNInfo", "Event"]


class ASNInfo(BaseModel):
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
    asn_info: List[ASNInfo]

    events: List[Event]
