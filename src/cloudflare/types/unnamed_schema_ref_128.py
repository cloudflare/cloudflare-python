# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UnnamedSchemaRef128"]


class UnnamedSchemaRef128(BaseModel):
    i_pv4: str = FieldInfo(alias="IPv4")

    i_pv6: str = FieldInfo(alias="IPv6")
