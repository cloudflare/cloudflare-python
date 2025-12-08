# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SuperBotFightModeLikelyConfiguration", "StaleZoneConfiguration"]


class StaleZoneConfiguration(BaseModel):
    """
    A read-only field that shows which unauthorized settings are currently active on the zone. These settings typically result from upgrades or downgrades.
    """

    fight_mode: Optional[bool] = None
    """Indicates that the zone's Bot Fight Mode is turned on."""


class SuperBotFightModeLikelyConfiguration(BaseModel):
    ai_bots_protection: Optional[Literal["block", "disabled", "only_on_ad_pages"]] = None
    """Enable rule to block AI Scrapers and Crawlers.

    Please note the value `only_on_ad_pages` is currently not available for
    Enterprise customers.
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

    optimize_wordpress: Optional[bool] = None
    """Whether to optimize Super Bot Fight Mode protections for Wordpress."""

    sbfm_definitely_automated: Optional[Literal["allow", "block", "managed_challenge"]] = None
    """Super Bot Fight Mode (SBFM) action to take on definitely automated requests."""

    sbfm_likely_automated: Optional[Literal["allow", "block", "managed_challenge"]] = None
    """Super Bot Fight Mode (SBFM) action to take on likely automated requests."""

    sbfm_static_resource_protection: Optional[bool] = None
    """
    Super Bot Fight Mode (SBFM) to enable static resource protection. Enable if
    static resources on your application need bot protection. Note: Static resource
    protection can also result in legitimate traffic being blocked.
    """

    sbfm_verified_bots: Optional[Literal["allow", "block"]] = None
    """Super Bot Fight Mode (SBFM) action to take on verified bots requests."""

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
