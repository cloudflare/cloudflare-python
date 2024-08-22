# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["WANStaticAddressing"]

class WANStaticAddressing(BaseModel):
    address: str
    """A valid CIDR notation representing an IP range."""

    gateway_address: str
    """A valid IPv4 address."""

    secondary_address: Optional[str] = None
    """A valid CIDR notation representing an IP range."""