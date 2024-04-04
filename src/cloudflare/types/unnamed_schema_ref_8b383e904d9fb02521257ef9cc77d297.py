# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UnnamedSchemaRef8b383e904d9fb02521257ef9cc77d297"]


class UnnamedSchemaRef8b383e904d9fb02521257ef9cc77d297(BaseModel):
    i_pv4: str = FieldInfo(alias="IPv4")

    i_pv6: str = FieldInfo(alias="IPv6")
