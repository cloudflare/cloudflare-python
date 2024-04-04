# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UnnamedSchemaRef4124a22436f90127c7fa2c4543219752"]


class UnnamedSchemaRef4124a22436f90127c7fa2c4543219752(BaseModel):
    client_asn: int = FieldInfo(alias="clientASN")

    client_as_name: str = FieldInfo(alias="clientASName")

    value: str
