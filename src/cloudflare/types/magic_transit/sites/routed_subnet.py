# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from .nat import Nat

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["RoutedSubnet"]


class RoutedSubnet(BaseModel):
    next_hop: str
    """A valid IPv4 address."""

    prefix: str
    """A valid CIDR notation representing an IP range."""

    nat: Optional[Nat] = None
