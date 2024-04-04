# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UnnamedSchemaRef9002274ed7cb7f3dc567421e31529a3a"]


class UnnamedSchemaRef9002274ed7cb7f3dc567421e31529a3a(BaseModel):
    i_pv4: List[str] = FieldInfo(alias="IPv4")

    i_pv6: List[str] = FieldInfo(alias="IPv6")

    timestamps: List[str]
