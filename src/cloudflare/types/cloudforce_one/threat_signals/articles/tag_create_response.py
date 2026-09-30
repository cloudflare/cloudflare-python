# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["TagCreateResponse"]


class TagCreateResponse(BaseModel):
    applied_by: Literal["ai", "analyst", "system"]

    category_id: Optional[str] = FieldInfo(alias="categoryId", default=None)

    uuid: str

    value: str
