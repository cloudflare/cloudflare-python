# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["TimeseriesGroupProtocolResponse", "Serie0"]


class Serie0(BaseModel):
    tcp: List[str]

    udp: List[str]


class TimeseriesGroupProtocolResponse(BaseModel):
    meta: object

    serie_0: Serie0
