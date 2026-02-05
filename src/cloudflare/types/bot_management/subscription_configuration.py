# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SubscriptionConfiguration", "StaleZoneConfiguration"]


class StaleZoneConfiguration(BaseModel):
    """
    A read-only field that shows which unauthorized settings are currently active on the zone. These settings typically result from upgrades or downgrades.
    """

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
    ai_bots_protection: Optional[Literal["block", "disabled", "only_on_ad_pages"]] = None
    """Enable rule to block AI Scrapers and Crawlers.

    Please note the value `only_on_ad_pages` is currently not available for
    Enterprise customers.
    """

    auto_update_model: Optional[bool] = None
    """
    Automatically update to the newest bot detection models created by Cloudflare as
    they are released.
    [Learn more.](https://developers.cloudflare.com/bots/reference/machine-learning-models#model-versions-and-release-notes)
    """

    bm_cookie_enabled: Optional[bool] = None
    """
    Indicates that the bot management cookie can be placed on end user devices
    accessing the site. Defaults to true
    """

    cf_robots_variant: Optional[Literal["off", "policy_only"]] = None
    """Specifies the Robots Access Control License variant to use."""

    crawler_protection: Optional[Literal["enabled", "disabled"]] = None
    """Enable rule to punish AI Scrapers and Crawlers via a link maze."""

    enable_js: Optional[bool] = None
    """Use lightweight, invisible JavaScript detections to improve Bot Management.

    [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).
    """

    is_robots_txt_managed: Optional[bool] = None
    """Enable cloudflare managed robots.txt.

    If an existing robots.txt is detected, then managed robots.txt will be prepended
    to the existing robots.txt.
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
