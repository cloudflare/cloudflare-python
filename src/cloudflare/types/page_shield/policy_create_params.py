# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PolicyCreateParams"]


class PolicyCreateParams(TypedDict, total=False):
    action: Literal["allow", "log"]
    """The action to take if the expression matches"""

    description: str
    """A description for the policy"""

    enabled: bool
    """Whether the policy is enabled"""

    expression: str
    """
    The expression which must match for the policy to be applied, using the
    Cloudflare Firewall rule expression syntax
    """

    value: str
    """The policy which will be applied"""
