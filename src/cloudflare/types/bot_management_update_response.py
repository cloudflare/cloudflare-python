# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "BotManagementUpdateResponse",
    "BotManagementBotFightModeConfig",
    "BotManagementSbfmDefinitelyConfig",
    "BotManagementSbfmLikelyConfig",
    "BotManagementBmSubscriptionConfig",
]


class BotManagementBotFightModeConfig(BaseModel):
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


class BotManagementSbfmDefinitelyConfig(BaseModel):
    enable_js: Optional[bool] = None
    """Use lightweight, invisible JavaScript detections to improve Bot Management.

    [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).
    """

    optimize_wordpress: Optional[bool] = None
    """Whether to optimize Super Bot Fight Mode protections for Wordpress."""

    sbfm_definitely_automated: Optional[Literal["allow", "block", "managed_challenge"]] = None
    """Super Bot Fight Mode (SBFM) action to take on definitely automated requests."""

    sbfm_static_resource_protection: Optional[bool] = None
    """
    Super Bot Fight Mode (SBFM) to enable static resource protection. Enable if
    static resources on your application need bot protection. Note: Static resource
    protection can also result in legitimate traffic being blocked.
    """

    sbfm_verified_bots: Optional[Literal["allow", "block"]] = None
    """Super Bot Fight Mode (SBFM) action to take on verified bots requests."""

    using_latest_model: Optional[bool] = None
    """
    A read-only field that indicates whether the zone currently is running the
    latest ML model.
    """


class BotManagementSbfmLikelyConfig(BaseModel):
    enable_js: Optional[bool] = None
    """Use lightweight, invisible JavaScript detections to improve Bot Management.

    [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).
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

    using_latest_model: Optional[bool] = None
    """
    A read-only field that indicates whether the zone currently is running the
    latest ML model.
    """


class BotManagementBmSubscriptionConfig(BaseModel):
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


BotManagementUpdateResponse = Union[
    BotManagementBotFightModeConfig,
    BotManagementSbfmDefinitelyConfig,
    BotManagementSbfmLikelyConfig,
    BotManagementBmSubscriptionConfig,
]
