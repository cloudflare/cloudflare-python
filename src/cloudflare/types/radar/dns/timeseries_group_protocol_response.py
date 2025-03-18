# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["TimeseriesGroupProtocolResponse", "Serie0"]


class Serie0(BaseModel):
    https: List[str] = FieldInfo(alias="HTTPS")

    tcp: List[str] = FieldInfo(alias="TCP")

    tls: List[str] = FieldInfo(alias="TLS")

    udp: List[str] = FieldInfo(alias="UDP")


class TimeseriesGroupProtocolResponse(BaseModel):
    meta: object

    serie_0: Serie0
