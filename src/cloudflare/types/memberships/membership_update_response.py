# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional

from ..._models import BaseModel
from .membership import Membership

__all__ = ["MembershipUpdateResponse", "IamAPIResponseCommon"]


class IamAPIResponseCommon(BaseModel):
    result: Optional[Membership] = None


MembershipUpdateResponse = Union[IamAPIResponseCommon, IamAPIResponseCommon]
