# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["PrebuiltPolicyListResponse"]


class PrebuiltPolicyListResponse(BaseModel):
    applicable_destinations: List[Literal["NONE", "ZERO_TRUST_LIST"]]

    policy_description: str

    policy_name: str

    policy_string: str
