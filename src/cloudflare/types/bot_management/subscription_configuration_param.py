# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SubscriptionConfigurationParam"]


class SubscriptionConfigurationParam(TypedDict, total=False):
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
