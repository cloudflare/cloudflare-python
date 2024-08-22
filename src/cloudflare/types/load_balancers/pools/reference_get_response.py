# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from typing_extensions import Literal, TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ReferenceGetResponse", "ReferenceGetResponseItem"]

class ReferenceGetResponseItem(BaseModel):
    reference_type: Optional[Literal["*", "referral", "referrer"]] = None

    resource_id: Optional[str] = None

    resource_name: Optional[str] = None

    resource_type: Optional[str] = None

ReferenceGetResponse: TypeAlias = List[ReferenceGetResponseItem]