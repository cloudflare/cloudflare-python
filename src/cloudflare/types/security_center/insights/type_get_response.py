# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["TypeGetResponse", "TypeGetResponseItem"]


class TypeGetResponseItem(BaseModel):
    count: Optional[int] = None

    value: Optional[str] = None


TypeGetResponse: TypeAlias = List[TypeGetResponseItem]
