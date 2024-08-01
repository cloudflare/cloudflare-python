# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["LockdownIPConfigurationParam"]


class LockdownIPConfigurationParam(TypedDict, total=False):
    target: Literal["ip"]
    """The configuration target.

    You must set the target to `ip` when specifying an IP address in the Zone
    Lockdown rule.
    """

    value: str
    """The IP address to match.

    This address will be compared to the IP address of incoming requests.
    """
