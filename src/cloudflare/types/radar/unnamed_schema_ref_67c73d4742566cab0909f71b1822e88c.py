# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UnnamedSchemaRef67c73d4742566cab0909f71b1822e88c"]


class UnnamedSchemaRef67c73d4742566cab0909f71b1822e88c(BaseModel):
    fail: List[str] = FieldInfo(alias="FAIL")

    none: List[str] = FieldInfo(alias="NONE")

    pass_: List[str] = FieldInfo(alias="PASS")
