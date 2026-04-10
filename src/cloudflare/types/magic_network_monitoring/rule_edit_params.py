# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["RuleEditParams"]


class RuleEditParams(TypedDict, total=False):
    account_id: Required[str]

    automatic_advertisement: Required[Optional[bool]]
    """
    Toggle on if you would like Cloudflare to automatically advertise the IP
    Prefixes within the rule via Magic Transit when the rule is triggered. Only
    available for users of Magic Transit.
    """

    name: Required[str]
    """The name of the rule.

    Must be unique. Supports characters A-Z, a-z, 0-9, underscore (\\__), dash (-),
    period (.), and tilde (~). You can’t have a space in the rule name. Max 256
    characters.
    """

    prefixes: Required[SequenceNotStr[str]]

    type: Required[Literal["threshold", "zscore", "advanced_ddos"]]
    """MNM rule type."""

    bandwidth_threshold: float
    """The number of bits per second for the rule.

    When this value is exceeded for the set duration, an alert notification is sent.
    Minimum of 1 and no maximum.
    """

    duration: Literal["1m", "5m", "10m", "15m", "20m", "30m", "45m", "60m"]
    """
    The amount of time that the rule threshold must be exceeded to send an alert
    notification. The final value must be equivalent to one of the following 8
    values ["1m","5m","10m","15m","20m","30m","45m","60m"].
    """

    packet_threshold: float
    """The number of packets per second for the rule.

    When this value is exceeded for the set duration, an alert notification is sent.
    Minimum of 1 and no maximum.
    """

    prefix_match: Optional[Literal["exact", "subnet", "supernet"]]
    """
    Prefix match type to be applied for a prefix auto advertisement when using an
    advanced_ddos rule.
    """

    zscore_sensitivity: Optional[Literal["low", "medium", "high"]]
    """Level of sensitivity set for zscore rules."""

    zscore_target: Optional[Literal["bits", "packets"]]
    """Target of the zscore rule analysis."""
