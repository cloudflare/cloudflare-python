# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

from typing_extensions import TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["CurrentGetResponse", "CurrentGetResponseItem"]


class CurrentGetResponseItem(BaseModel):
    app_id: str = FieldInfo(alias="appID")
    """Application identifier."""

    bytes_egress: float = FieldInfo(alias="bytesEgress")
    """Number of bytes sent"""

    bytes_ingress: float = FieldInfo(alias="bytesIngress")
    """Number of bytes received"""

    connections: float
    """Number of connections"""

    duration_avg: float = FieldInfo(alias="durationAvg")
    """Average duration of connections"""


CurrentGetResponse: TypeAlias = List[CurrentGetResponseItem]
