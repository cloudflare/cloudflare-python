# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["IndexInfoResponse"]


class IndexInfoResponse(BaseModel):
    dimensions: Optional[int] = None
    """Specifies the number of dimensions for the index"""

    processed_up_to_datetime: Optional[datetime] = FieldInfo(alias="processedUpToDatetime", default=None)
    """
    Specifies the timestamp the last mutation batch was processed as an ISO8601
    string.
    """

    processed_up_to_mutation: Optional[str] = FieldInfo(alias="processedUpToMutation", default=None)
    """
    The unique identifier for the async mutation operation containing the changeset.
    """

    vector_count: Optional[int] = FieldInfo(alias="vectorCount", default=None)
    """Specifies the number of vectors present in the index"""
