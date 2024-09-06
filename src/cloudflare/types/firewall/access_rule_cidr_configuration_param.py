# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AccessRuleCIDRConfigurationParam"]


class AccessRuleCIDRConfigurationParam(TypedDict, total=False):
    target: Literal["ip_range"]
    """The configuration target.

    You must set the target to `ip_range` when specifying an IP address range in the
    rule.
    """

    value: str
    """The IP address range to match.

    You can only use prefix lengths `/16` and `/24` for IPv4 ranges, and prefix
    lengths `/32`, `/48`, and `/64` for IPv6 ranges.
    """
