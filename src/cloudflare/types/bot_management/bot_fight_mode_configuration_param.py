# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["BotFightModeConfigurationParam"]


class BotFightModeConfigurationParam(TypedDict, total=False):
    ai_bots_protection: Literal["block", "disabled", "only_on_ad_pages"]
    """Enable rule to block AI Scrapers and Crawlers.

    Please note the value `only_on_ad_pages` is currently not available for
    Enterprise customers.
    """

    cf_robots_variant: Literal["off", "policy_only"]
    """Specifies the Robots Access Control License variant to use."""

    crawler_protection: Literal["enabled", "disabled"]
    """Enable rule to punish AI Scrapers and Crawlers via a link maze."""

    enable_js: bool
    """Use lightweight, invisible JavaScript detections to improve Bot Management.

    [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).
    """

    fight_mode: bool
    """Whether to enable Bot Fight Mode."""

    is_robots_txt_managed: bool
    """Enable cloudflare managed robots.txt.

    If an existing robots.txt is detected, then managed robots.txt will be prepended
    to the existing robots.txt.
    """
