# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["IPV6ConfigurationParam"]


class IPV6ConfigurationParam(TypedDict, total=False):
    target: Literal["ip6"]
    """The configuration target.

    You must set the target to `ip6` when specifying an IPv6 address in the rule.
    """

    value: str
    """The IPv6 address to match."""
