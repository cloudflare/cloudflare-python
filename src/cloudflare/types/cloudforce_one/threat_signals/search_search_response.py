# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["SearchSearchResponse", "Result"]


class Result(BaseModel):
    article_id: str

    dataset_id: Optional[str] = None

    event_id: Optional[str] = None

    feed_id: str

    score: float

    text: str


class SearchSearchResponse(BaseModel):
    count: int
    """Number of unique article candidates returned in this response.

    Equal to results.length.
    """

    results: List[Result]
