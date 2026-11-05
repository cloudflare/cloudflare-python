# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PrecursorUpdateParams", "Rule"]


class PrecursorUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    cloudflare_version: Annotated[Literal["1.0"], PropertyInfo(alias="Cloudflare-Version")]

    mode: Literal["off", "monitor", "arm"]
    """Controls Precursor detection for the zone.

    `off` disables detection, `monitor` records detections without affecting bot
    scores, and `arm` allows detections to affect bot scores.
    """

    rules: Iterable[Rule]
    """The ordered list of Precursor rules for the zone."""

    show_interstitial: bool
    """Whether Precursor shows an interstitial when it takes action on a request."""


class Rule(TypedDict, total=False):
    expression: Required[str]
    """The filter expression that determines which requests the rule matches."""

    show_interstitial: Required[bool]
    """Whether Precursor shows an interstitial when it takes action on a request."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule is active."""
