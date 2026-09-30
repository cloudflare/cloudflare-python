# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["FeedPollResponse", "Feed"]


class Feed(BaseModel):
    feed_id: str

    status: Literal["workflow_created", "error"]

    workflow_id: str

    feed_enabled: Optional[bool] = None


class FeedPollResponse(BaseModel):
    errors: float

    feeds: List[Feed]

    triggered: float
