# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = ["EligibleGetResponse", "EligibleGetResponseItem"]


class EligibleGetResponseItem(BaseModel):
    eligible: Optional[bool] = None
    """Determines whether or not the account is eligible for the delivery mechanism."""

    ready: Optional[bool] = None
    """Beta flag.

    Users can create a policy with a mechanism that is not ready, but we cannot
    guarantee successful delivery of notifications.
    """

    type: Optional[Literal["email", "pagerduty", "webhook"]] = None
    """Determines type of delivery mechanism."""


EligibleGetResponse: TypeAlias = Dict[str, List[EligibleGetResponseItem]]
