# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel

__all__ = ["EventListResponse", "ASNInfo", "Event", "EventTag"]


class ASNInfo(BaseModel):
    asn: int

    country_code: str

    org_name: str


class EventTag(BaseModel):
    name: str

    score: int


class Event(BaseModel):
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

    tags: List[EventTag]

    victim_asns: List[int]

    victim_countries: List[str]


class EventListResponse(BaseModel):
    asn_info: List[ASNInfo]

    events: List[Event]

    total_monitors: int
