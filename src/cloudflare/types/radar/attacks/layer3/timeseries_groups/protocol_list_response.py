# File generated from our OpenAPI spec by Stainless.

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ......_models import BaseModel
from ......types import shared

__all__ = ["ProtocolListResponse", "Serie0"]


class Serie0(BaseModel):
    gre: List[str] = FieldInfo(alias="GRE")

    icmp: List[str] = FieldInfo(alias="ICMP")

    tcp: List[str] = FieldInfo(alias="TCP")

    timestamps: List[str]

    udp: List[str] = FieldInfo(alias="UDP")


class ProtocolListResponse(BaseModel):
    meta: object

    serie_0: Serie0
