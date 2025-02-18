# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = ["TelemetryGetResponse", "E", "EK", "EUnionMember8"]


class EK(BaseModel):
    k: Literal["Init"]
    """Initialized process"""


class EUnionMember8(BaseModel):
    k: Literal["StartUpgrade"]
    """Started upgrade"""

    url: str
    """Location of upgrade bundle"""


E: TypeAlias = Union[EK, EK, EK, EK, EK, EK, EK, EK, EUnionMember8, EK, EK, EK, EK]


class TelemetryGetResponse(BaseModel):
    e: E

    n: float
    """Sequence number, used to order events with the same timestamp"""

    t: float
    """Time the Event was recorded (seconds since the Unix epoch)"""
