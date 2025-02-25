# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MagicNetworkMonitoringRule"]


class MagicNetworkMonitoringRule(BaseModel):
    automatic_advertisement: Optional[bool] = None
    """
    Toggle on if you would like Cloudflare to automatically advertise the IP
    Prefixes within the rule via Magic Transit when the rule is triggered. Only
    available for users of Magic Transit.
    """

    name: str
    """The name of the rule.

    Must be unique. Supports characters A-Z, a-z, 0-9, underscore (\\__), dash (-),
    period (.), and tilde (~). You can’t have a space in the rule name. Max 256
    characters.
    """

    prefixes: List[str]

    type: Literal["threshold", "zscore", "advanced_ddos"]
    """MNM rule type."""

    id: Optional[str] = None
    """The id of the rule. Must be unique."""

    bandwidth_threshold: Optional[float] = None
    """The number of bits per second for the rule.

    When this value is exceeded for the set duration, an alert notification is sent.
    Minimum of 1 and no maximum.
    """

    duration: Optional[Literal["1m", "5m", "10m", "15m", "20m", "30m", "45m", "60m"]] = None
    """
    The amount of time that the rule threshold must be exceeded to send an alert
    notification. The final value must be equivalent to one of the following 8
    values ["1m","5m","10m","15m","20m","30m","45m","60m"].
    """

    packet_threshold: Optional[float] = None
    """The number of packets per second for the rule.

    When this value is exceeded for the set duration, an alert notification is sent.
    Minimum of 1 and no maximum.
    """

    prefix_match: Optional[Literal["exact", "subnet", "supernet"]] = None
    """
    Prefix match type to be applied for a prefix auto advertisement when using an
    advanced_ddos rule.
    """

    zscore_sensitivity: Optional[Literal["low", "medium", "high"]] = None
    """Level of sensitivity set for zscore rules."""

    zscore_target: Optional[Literal["bits", "packets"]] = None
    """Target of the zscore rule analysis."""
