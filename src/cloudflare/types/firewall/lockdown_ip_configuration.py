# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["LockdownIPConfiguration"]

class LockdownIPConfiguration(BaseModel):
    target: Optional[Literal["ip"]] = None
    """The configuration target.

    You must set the target to `ip` when specifying an IP address in the Zone
    Lockdown rule.
    """

    value: Optional[str] = None
    """The IP address to match.

    This address will be compared to the IP address of incoming requests.
    """