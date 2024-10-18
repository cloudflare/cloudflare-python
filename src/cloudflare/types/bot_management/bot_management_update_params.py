# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "BotManagementUpdateParams",
    "BotFightModeConfiguration",
    "SuperBotFightModeDefinitelyConfiguration",
    "SuperBotFightModeLikelyConfiguration",
    "SubscriptionConfiguration",
]


class BotFightModeConfiguration(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    ai_bots_protection: Literal["block", "disabled"]
    """Enable rule to block AI Scrapers and Crawlers."""

    enable_js: bool
    """Use lightweight, invisible JavaScript detections to improve Bot Management.

    [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).
    """

    fight_mode: bool
    """Whether to enable Bot Fight Mode."""


class SuperBotFightModeDefinitelyConfiguration(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    ai_bots_protection: Literal["block", "disabled"]
    """Enable rule to block AI Scrapers and Crawlers."""

    enable_js: bool
    """Use lightweight, invisible JavaScript detections to improve Bot Management.

    [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).
    """

    optimize_wordpress: bool
    """Whether to optimize Super Bot Fight Mode protections for Wordpress."""

    sbfm_definitely_automated: Literal["allow", "block", "managed_challenge"]
    """Super Bot Fight Mode (SBFM) action to take on definitely automated requests."""

    sbfm_static_resource_protection: bool
    """
    Super Bot Fight Mode (SBFM) to enable static resource protection. Enable if
    static resources on your application need bot protection. Note: Static resource
    protection can also result in legitimate traffic being blocked.
    """

    sbfm_verified_bots: Literal["allow", "block"]
    """Super Bot Fight Mode (SBFM) action to take on verified bots requests."""


class SuperBotFightModeLikelyConfiguration(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    ai_bots_protection: Literal["block", "disabled"]
    """Enable rule to block AI Scrapers and Crawlers."""

    enable_js: bool
    """Use lightweight, invisible JavaScript detections to improve Bot Management.

    [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).
    """

    optimize_wordpress: bool
    """Whether to optimize Super Bot Fight Mode protections for Wordpress."""

    sbfm_definitely_automated: Literal["allow", "block", "managed_challenge"]
    """Super Bot Fight Mode (SBFM) action to take on definitely automated requests."""

    sbfm_likely_automated: Literal["allow", "block", "managed_challenge"]
    """Super Bot Fight Mode (SBFM) action to take on likely automated requests."""

    sbfm_static_resource_protection: bool
    """
    Super Bot Fight Mode (SBFM) to enable static resource protection. Enable if
    static resources on your application need bot protection. Note: Static resource
    protection can also result in legitimate traffic being blocked.
    """

    sbfm_verified_bots: Literal["allow", "block"]
    """Super Bot Fight Mode (SBFM) action to take on verified bots requests."""


class SubscriptionConfiguration(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    ai_bots_protection: Literal["block", "disabled"]
    """Enable rule to block AI Scrapers and Crawlers."""

    auto_update_model: bool
    """
    Automatically update to the newest bot detection models created by Cloudflare as
    they are released.
    [Learn more.](https://developers.cloudflare.com/bots/reference/machine-learning-models#model-versions-and-release-notes)
    """

    enable_js: bool
    """Use lightweight, invisible JavaScript detections to improve Bot Management.

    [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).
    """

    suppress_session_score: bool
    """
    Whether to disable tracking the highest bot score for a session in the Bot
    Management cookie.
    """


BotManagementUpdateParams: TypeAlias = Union[
    BotFightModeConfiguration,
    SuperBotFightModeDefinitelyConfiguration,
    SuperBotFightModeLikelyConfiguration,
    SubscriptionConfiguration,
]
