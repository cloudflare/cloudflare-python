# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SubscriptionConfiguration", "StaleZoneConfiguration"]


class StaleZoneConfiguration(BaseModel):
    fight_mode: Optional[bool] = None
    """Indicates that the zone's Bot Fight Mode is turned on."""

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


class SubscriptionConfiguration(BaseModel):
    ai_bots_protection: Optional[Literal["block", "disabled"]] = None
    """Enable rule to block AI Scrapers and Crawlers."""

    auto_update_model: Optional[bool] = None
    """
    Automatically update to the newest bot detection models created by Cloudflare as
    they are released.
    [Learn more.](https://developers.cloudflare.com/bots/reference/machine-learning-models#model-versions-and-release-notes)
    """

    enable_js: Optional[bool] = None
    """Use lightweight, invisible JavaScript detections to improve Bot Management.

    [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).
    """

    stale_zone_configuration: Optional[StaleZoneConfiguration] = None
    """
    A read-only field that shows which unauthorized settings are currently active on
    the zone. These settings typically result from upgrades or downgrades.
    """

    suppress_session_score: Optional[bool] = None
    """
    Whether to disable tracking the highest bot score for a session in the Bot
    Management cookie.
    """

    using_latest_model: Optional[bool] = None
    """
    A read-only field that indicates whether the zone currently is running the
    latest ML model.
    """
