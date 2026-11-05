# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PrecursorConfig", "Rule"]


class Rule(BaseModel):
    expression: str
    """The filter expression that determines which requests the rule matches."""

    show_interstitial: bool
    """Whether Precursor shows an interstitial when it takes action on a request."""

    id: Optional[str] = None
    """The read-only identifier that Cloudflare assigns to the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    enabled: Optional[bool] = None
    """Whether the rule is active."""


class PrecursorConfig(BaseModel):
    mode: Optional[Literal["off", "monitor", "arm"]] = None
    """Controls Precursor detection for the zone.

    `off` disables detection, `monitor` records detections without affecting bot
    scores, and `arm` allows detections to affect bot scores.
    """

    rules: Optional[List[Rule]] = None
    """The ordered list of Precursor rules for the zone."""

    show_interstitial: Optional[bool] = None
    """Whether Precursor shows an interstitial when it takes action on a request."""
