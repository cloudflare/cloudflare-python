# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = [
    "ReferenceAccountLoadBalancerPoolsListPoolReferencesResponse",
    "ReferenceAccountLoadBalancerPoolsListPoolReferencesResponseItem",
]


class ReferenceAccountLoadBalancerPoolsListPoolReferencesResponseItem(BaseModel):
    reference_type: Optional[Literal["*", "referral", "referrer"]] = None

    resource_id: Optional[str] = None

    resource_name: Optional[str] = None

    resource_type: Optional[str] = None


ReferenceAccountLoadBalancerPoolsListPoolReferencesResponse = List[
    ReferenceAccountLoadBalancerPoolsListPoolReferencesResponseItem
]
