# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["LockdownCIDRConfigurationParam"]


class LockdownCIDRConfigurationParam(TypedDict, total=False):
    target: Literal["ip_range"]
    """The configuration target.

    You must set the target to `ip_range` when specifying an IP address range in the
    Zone Lockdown rule.
    """

    value: str
    """The IP address range to match. You can only use prefix lengths `/16` and `/24`."""
