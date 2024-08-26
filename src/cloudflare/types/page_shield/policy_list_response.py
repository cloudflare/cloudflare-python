# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["PolicyListResponse"]

class PolicyListResponse(BaseModel):
    id: str
    """Identifier"""

    action: Literal["allow", "log"]
    """The action to take if the expression matches"""

    description: str
    """A description for the policy"""

    enabled: bool
    """Whether the policy is enabled"""

    expression: str
    """
    The expression which must match for the policy to be applied, using the
    Cloudflare Firewall rule expression syntax
    """

    value: str
    """The policy which will be applied"""