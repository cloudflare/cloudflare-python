# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["IPV6Configuration"]


class IPV6Configuration(BaseModel):
    target: Optional[Literal["ip6"]] = None
    """The configuration target.

    You must set the target to `ip6` when specifying an IPv6 address in the rule.
    """

    value: Optional[str] = None
    """The IPv6 address to match."""
