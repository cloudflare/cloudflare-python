# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BotFightModeConfiguration", "AIAgents", "StaleZoneConfiguration"]


class AIAgents(BaseModel):
    """Configure blocking behavior for supported personal AI agents."""

    anthropic_agent: Optional[Literal["disabled", "block", "only_on_ad_pages"]] = None
    """Action to apply to one supported personal AI agent."""

    google_agent: Optional[Literal["disabled", "block", "only_on_ad_pages"]] = None
    """Action to apply to one supported personal AI agent."""

    instinct: Optional[Literal["disabled", "block", "only_on_ad_pages"]] = None
    """Action to apply to one supported personal AI agent."""

    muse: Optional[Literal["disabled", "block", "only_on_ad_pages"]] = None
    """Action to apply to one supported personal AI agent."""

    openai_agent: Optional[Literal["disabled", "block", "only_on_ad_pages"]] = None
    """Action to apply to one supported personal AI agent."""


class StaleZoneConfiguration(BaseModel):
    """
    A read-only field that shows which unauthorized settings are currently active on the zone. These settings typically result from upgrades or downgrades.
    """

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

    suppress_session_score: Optional[bool] = None
    """Indicates that the zone's session score tracking is disabled."""


class BotFightModeConfiguration(BaseModel):
    ai_agents: Optional[AIAgents] = None
    """Configure blocking behavior for supported personal AI agents."""

    ai_bots_migration_opt_out: Optional[bool] = None
    """
    Temporary migration flag tracking zones opted out of AI bots managed-rule
    updates.
    """

    ai_bots_protection: Optional[Literal["block", "disabled", "only_on_ad_pages"]] = None
    """Enable rule to block AI Scrapers and Crawlers."""

    aisearch: Optional[Literal["disabled", "block", "only_on_ad_pages"]] = FieldInfo(alias="ai_search", default=None)
    """Configure robots.txt policy for AI search bots."""

    ai_training: Optional[Literal["disabled", "disallow", "block", "only_on_ad_pages"]] = None
    """Configure robots.txt policy for AI model training bots."""

    ai_user: Optional[Literal["disabled", "block", "only_on_ad_pages"]] = None
    """Configure robots.txt policy for AI assistant and agent bots."""

    bot_preference_sync_enabled: Optional[bool] = None
    """Enable Bot Preference Sync for this zone.

    When enabled, Cloudflare can serve robots.txt content derived from the zone's AI
    Search, AI User, and AI Training preferences.
    """

    cf_robots_variant: Optional[Literal["off", "policy_only"]] = None
    """Specifies the Robots Access Control License variant to use."""

    content_bots_protection: Optional[Literal["block", "disabled"]] = None
    """Enable rule to block content bots.

    When enabled, blocks automated traffic with low bot scores, excluding safe
    verified bot categories. Exceptions should be managed via skip rules.
    """

    crawler_protection: Optional[Literal["enabled", "disabled"]] = None
    """Enable rule to punish AI Scrapers and Crawlers via a link maze."""

    enable_js: Optional[bool] = None
    """Use lightweight, invisible JavaScript detections to improve Bot Management.

    [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).
    """

    fight_mode: Optional[bool] = None
    """Whether to enable Bot Fight Mode."""

    is_robots_txt_managed: Optional[bool] = None
    """Enable cloudflare managed robots.txt.

    If an existing robots.txt is detected, then managed robots.txt will be prepended
    to the existing robots.txt.
    """

    jsd_api_results_enabled: Optional[bool] = None
    """
    Whether to use JavaScript Detection results submitted through the API for this
    zone.
    """

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
