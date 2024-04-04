# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UnnamedSchemaRef154"]


class UnnamedSchemaRef154(BaseModel):
    client_asn: int = FieldInfo(alias="clientASN")

    client_as_name: str = FieldInfo(alias="clientASName")

    value: str
