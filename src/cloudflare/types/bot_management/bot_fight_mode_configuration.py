# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BotFightModeConfiguration", "StaleZoneConfiguration"]


class StaleZoneConfiguration(BaseModel):
    optimize_wordpress: Optional[bool] = None
    """Indicates that the zone's wordpress optimization for SBFM is turned on."""

    sbfm_definitely_automated: Optional[str] = None
    """
    Indicates that the zone's definitely automated requests are being blocked or
    challenged.
    """

    sbfm_likely_automated: Optional[str] = None
    """
    Indicates that the zone's likely automated requests are being blocked or
    challenged.
    """

    sbfm_static_resource_protection: Optional[str] = None
    """Indicates that the zone's static resource protection is turned on."""

    sbfm_verified_bots: Optional[str] = None
    """Indicates that the zone's verified bot requests are being blocked."""

    suppress_session_score: Optional[bool] = None
    """Indicates that the zone's session score tracking is disabled."""


class BotFightModeConfiguration(BaseModel):
    ai_bots_protection: Optional[Literal["block", "disabled"]] = None
    """Enable rule to block AI Scrapers and Crawlers."""

    enable_js: Optional[bool] = None
    """Use lightweight, invisible JavaScript detections to improve Bot Management.

    [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).
    """

    fight_mode: Optional[bool] = None
    """Whether to enable Bot Fight Mode."""

    stale_zone_configuration: Optional[StaleZoneConfiguration] = None
    """
    A read-only field that shows which unauthorized settings are currently active on
    the zone. These settings typically result from upgrades or downgrades.
    """

    using_latest_model: Optional[bool] = None
    """
    A read-only field that indicates whether the zone currently is running the
    latest ML model.
    """
