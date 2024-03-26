# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["MagicVisibilityMNMRule"]


class MagicVisibilityMNMRule(BaseModel):
    automatic_advertisement: Optional[bool] = None
    """
    Toggle on if you would like Cloudflare to automatically advertise the IP
    Prefixes within the rule via Magic Transit when the rule is triggered. Only
    available for users of Magic Transit.
    """

    duration: str
    """
    The amount of time that the rule threshold must be exceeded to send an alert
    notification. The final value must be equivalent to one of the following 8
    values ["1m","5m","10m","15m","20m","30m","45m","60m"]. The format is
    AhBmCsDmsEusFns where A, B, C, D, E and F durations are optional; however at
    least one unit must be provided.
    """

    name: str
    """The name of the rule.

    Must be unique. Supports characters A-Z, a-z, 0-9, underscore (\\__), dash (-),
    period (.), and tilde (~). You can’t have a space in the rule name. Max 256
    characters.
    """

    prefixes: List[str]

    id: Optional[str] = None

    bandwidth_threshold: Optional[float] = None
    """The number of bits per second for the rule.

    When this value is exceeded for the set duration, an alert notification is sent.
    Minimum of 1 and no maximum.
    """

    packet_threshold: Optional[float] = None
    """The number of packets per second for the rule.

    When this value is exceeded for the set duration, an alert notification is sent.
    Minimum of 1 and no maximum.
    """
