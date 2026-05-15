# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RuleCreateParams"]


class RuleCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    burst_sensitivity: Required[str]
    """The burst sensitivity. Must be one of 'low', 'medium', 'high'."""

    mode: Required[str]
    """The mode for SYN Protection.

    Must be one of 'enabled', 'disabled', 'monitoring'.
    """

    name: Required[str]
    """The name of the SYN Protection rule.

    Value is relative to the 'scope' setting. For 'global' scope, name should be
    'global'. For either the 'region' or 'datacenter' scope, name should be the
    actual name of the region or datacenter, e.g., 'wnam' or 'lax'.
    """

    rate_sensitivity: Required[str]
    """The rate sensitivity. Must be one of 'low', 'medium', 'high'."""

    scope: Required[str]
    """The scope for the SYN Protection rule.

    Must be one of 'global', 'region', or 'datacenter'.
    """

    mitigation_type: str
    """The type of mitigation.

    Must be one of 'challenge' or 'retransmit'. Optional. Defaults to 'challenge'.
    """
