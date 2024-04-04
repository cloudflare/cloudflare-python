# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UnnamedSchemaRef134"]


class UnnamedSchemaRef134(BaseModel):
    id: int

    name: str

    super_category_id: Optional[int] = None
