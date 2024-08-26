# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["TimeseriesGroupTLSVersionResponse", "Serie0"]


class Serie0(BaseModel):
    tls_1_0: List[str] = FieldInfo(alias="TLS 1.0")

    tls_1_1: List[str] = FieldInfo(alias="TLS 1.1")

    tls_1_2: List[str] = FieldInfo(alias="TLS 1.2")

    tls_1_3: List[str] = FieldInfo(alias="TLS 1.3")


class TimeseriesGroupTLSVersionResponse(BaseModel):
    meta: object

    serie_0: Serie0
