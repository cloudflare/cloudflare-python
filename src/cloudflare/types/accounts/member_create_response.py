# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional

from ..._models import BaseModel
from ..shared.member import Member

__all__ = ["MemberCreateResponse", "IamAPIResponseCommon"]


class IamAPIResponseCommon(BaseModel):
    result: Optional[Member] = None


MemberCreateResponse = Union[IamAPIResponseCommon, IamAPIResponseCommon]
