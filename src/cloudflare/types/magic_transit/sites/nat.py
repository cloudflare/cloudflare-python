# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["Nat"]


class Nat(BaseModel):
    static_prefix: Optional[str] = None
    """A valid CIDR notation representing an IP range."""
