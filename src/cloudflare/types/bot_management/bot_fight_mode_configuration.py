# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BotFightModeConfiguration"]


class BotFightModeConfiguration(BaseModel):
    ai_bots_protection: Optional[Literal["block", "disabled"]] = None
    """Enable rule to block AI Scrapers and Crawlers."""

    enable_js: Optional[bool] = None
    """Use lightweight, invisible JavaScript detections to improve Bot Management.

    [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).
    """

    fight_mode: Optional[bool] = None
    """Whether to enable Bot Fight Mode."""

    using_latest_model: Optional[bool] = None
    """
    A read-only field that indicates whether the zone currently is running the
    latest ML model.
    """
