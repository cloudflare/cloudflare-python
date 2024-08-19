# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["LockdownCIDRConfiguration"]


class LockdownCIDRConfiguration(BaseModel):
    target: Optional[Literal["ip_range"]] = None
    """The configuration target.

    You must set the target to `ip_range` when specifying an IP address range in the
    Zone Lockdown rule.
    """

    value: Optional[str] = None
    """The IP address range to match. You can only use prefix lengths `/16` and `/24`."""
