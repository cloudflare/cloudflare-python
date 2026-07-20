# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["CategoryCreateResponse"]


class CategoryCreateResponse(BaseModel):
    name: str

    uuid: str

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)
