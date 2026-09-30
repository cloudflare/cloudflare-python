# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["FeedCreateParams"]


class FeedCreateParams(TypedDict, total=False):
    account_id: Required[str]

    category_id: Optional[
        Literal[
            "b12a0fd6-f7b9-5393-9ef3-f888d506c550",
            "d5b70eaa-626f-5761-b55b-6d9590df49fb",
            "3b572d2b-890d-5286-9433-f18c85079030",
            "17f90d3b-37d3-5241-8ad4-7d6abbc2006c",
            "c68f28e9-7e8f-5d4b-853b-f3076893a9ee",
            "bb0e4a94-38ab-5c14-80a7-28cee9f4b139",
            "b1ef66d9-a73c-58dc-b269-22d34dfd11f4",
            "ab02a976-0a20-5c76-a553-7f6325afacfe",
        ]
    ]
    """
    One of the predefined Threat Signals feed categories; see GET
    /:account_id/v2/threat-signals/categories.
    """

    curated_feed_id: str

    display_name: Optional[str]

    enabled: bool

    poll_interval_s: int

    title: Optional[str]

    url: str
