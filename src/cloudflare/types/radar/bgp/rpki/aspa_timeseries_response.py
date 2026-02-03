# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["ASPATimeseriesResponse", "Meta", "Serie0"]


class Meta(BaseModel):
    data_time: datetime = FieldInfo(alias="dataTime")
    """Timestamp of the underlying data."""

    query_time: datetime = FieldInfo(alias="queryTime")
    """Timestamp when the query was executed."""


class Serie0(BaseModel):
    timestamps: List[datetime]

    values: List[str]


class ASPATimeseriesResponse(BaseModel):
    meta: Meta

    serie_0: Serie0
