# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional, List

from typing_extensions import Literal, TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

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
