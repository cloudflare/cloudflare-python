# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["TagGenerateResponse", "Tag"]


class Tag(BaseModel):
    applied_by: Literal["ai", "analyst", "system"]

    category_id: Optional[str] = FieldInfo(alias="categoryId", default=None)

    uuid: str

    value: str


class TagGenerateResponse(BaseModel):
    tag_skill_version: str

    tags: List[Tag]
    """
    Final hydrated assignment set; may be empty when no applicable tags are
    selected.
    """
