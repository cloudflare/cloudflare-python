# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["VectorizeIndexQuery", "Match"]


class Match(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    metadata: Optional[object] = None

    score: Optional[float] = None
    """The score of the vector according to the index's distance metric"""

    values: Optional[List[float]] = None


class VectorizeIndexQuery(BaseModel):
    count: Optional[int] = None
    """Specifies the count of vectors returned by the search"""

    matches: Optional[List[Match]] = None
    """Array of vectors matched by the search"""
