# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["BotFightModeConfigurationParam"]


class BotFightModeConfigurationParam(TypedDict, total=False):
    ai_bots_protection: Literal["block", "disabled"]
    """Enable rule to block AI Scrapers and Crawlers."""

    enable_js: bool
    """Use lightweight, invisible JavaScript detections to improve Bot Management.

    [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).
    """

    fight_mode: bool
    """Whether to enable Bot Fight Mode."""
