# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = ["ReferenceGetResponse", "ReferenceGetResponseItem"]


class ReferenceGetResponseItem(BaseModel):
    reference_type: Optional[Literal["*", "referral", "referrer"]] = None

    resource_id: Optional[str] = None

    resource_name: Optional[str] = None

    resource_type: Optional[str] = None


ReferenceGetResponse: TypeAlias = List[ReferenceGetResponseItem]
