# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["ASNAsSetResponse", "AsSet"]


class AsSet(BaseModel):
    as_members_count: int
    """The number of AS members in the AS-SET"""

    as_set_members_count: int
    """The number of AS-SET members in the AS-SET"""

    as_set_upstreams_count: int
    """The number of recursive upstream AS-SETs"""

    asn_cone_size: int
    """The number of unique ASNs in the AS-SETs recursive downstream"""

    irr_sources: List[str]
    """The IRR sources of the AS-SET"""

    name: str
    """The name of the AS-SET"""

    asn: Optional[int] = None
    """The inferred AS number of the AS-SET"""


class ASNAsSetResponse(BaseModel):
    as_sets: List[AsSet]

    paths: List[List[str]]
    """Paths from the AS-SET that include the given AS to its upstreams recursively"""
