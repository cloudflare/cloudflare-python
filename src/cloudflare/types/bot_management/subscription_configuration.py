# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SubscriptionConfiguration"]


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
