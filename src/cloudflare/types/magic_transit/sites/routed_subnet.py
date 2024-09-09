# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .nat import Nat
from ...._models import BaseModel

__all__ = ["RoutedSubnet"]


class RoutedSubnet(BaseModel):
    next_hop: str
    """A valid IPv4 address."""

    prefix: str
    """A valid CIDR notation representing an IP range."""

    nat: Optional[Nat] = None
