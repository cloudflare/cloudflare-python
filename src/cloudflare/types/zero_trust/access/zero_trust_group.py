# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional, List

from datetime import datetime

from ..access_rule import AccessRule

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ZeroTrustGroup"]

class ZeroTrustGroup(BaseModel):
    id: Optional[str] = None
    """UUID"""

    created_at: Optional[datetime] = None

    exclude: Optional[List[AccessRule]] = None
    """Rules evaluated with a NOT logical operator.

    To match a policy, a user cannot meet any of the Exclude rules.
    """

    include: Optional[List[AccessRule]] = None
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    is_default: Optional[List[AccessRule]] = None
    """Rules evaluated with an AND logical operator.

    To match a policy, a user must meet all of the Require rules.
    """

    name: Optional[str] = None
    """The name of the Access group."""

    require: Optional[List[AccessRule]] = None
    """Rules evaluated with an AND logical operator.

    To match a policy, a user must meet all of the Require rules.
    """

    updated_at: Optional[datetime] = None