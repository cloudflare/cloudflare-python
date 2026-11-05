# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SuperBotFightModeLikelyConfigurationParam", "AIAgents"]


class AIAgents(TypedDict, total=False):
    """Configure blocking behavior for supported personal AI agents."""

    anthropic_agent: Literal["disabled", "block", "only_on_ad_pages"]
    """Action to apply to one supported personal AI agent."""

    google_agent: Literal["disabled", "block", "only_on_ad_pages"]
    """Action to apply to one supported personal AI agent."""

    instinct: Literal["disabled", "block", "only_on_ad_pages"]
    """Action to apply to one supported personal AI agent."""

    muse: Literal["disabled", "block", "only_on_ad_pages"]
    """Action to apply to one supported personal AI agent."""

    openai_agent: Literal["disabled", "block", "only_on_ad_pages"]
    """Action to apply to one supported personal AI agent."""


class SuperBotFightModeLikelyConfigurationParam(TypedDict, total=False):
    ai_agents: AIAgents
    """Configure blocking behavior for supported personal AI agents."""

    ai_bots_migration_opt_out: bool
    """
    Temporary migration flag tracking zones opted out of AI bots managed-rule
    updates.
    """

    ai_bots_protection: Literal["block", "disabled", "only_on_ad_pages"]
    """Enable rule to block AI Scrapers and Crawlers."""

    aisearch: Annotated[Literal["disabled", "block", "only_on_ad_pages"], PropertyInfo(alias="ai_search")]
    """Configure robots.txt policy for AI search bots."""

    ai_training: Literal["disabled", "disallow", "block", "only_on_ad_pages"]
    """Configure robots.txt policy for AI model training bots."""

    ai_user: Literal["disabled", "block", "only_on_ad_pages"]
    """Configure robots.txt policy for AI assistant and agent bots."""

    bot_preference_sync_enabled: bool
    """Enable Bot Preference Sync for this zone.

    When enabled, Cloudflare can serve robots.txt content derived from the zone's AI
    Search, AI User, and AI Training preferences.
    """

    cf_robots_variant: Literal["off", "policy_only"]
    """Specifies the Robots Access Control License variant to use."""

    content_bots_protection: Literal["block", "disabled"]
    """Enable rule to block content bots.

    When enabled, blocks automated traffic with low bot scores, excluding safe
    verified bot categories. Exceptions should be managed via skip rules.
    """

    crawler_protection: Literal["enabled", "disabled"]
    """Enable rule to punish AI Scrapers and Crawlers via a link maze."""

    enable_js: bool
    """Use lightweight, invisible JavaScript detections to improve Bot Management.

    [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).
    """

    is_robots_txt_managed: bool
    """Enable cloudflare managed robots.txt.

    If an existing robots.txt is detected, then managed robots.txt will be prepended
    to the existing robots.txt.
    """

    jsd_api_results_enabled: bool
    """
    Whether to use JavaScript Detection results submitted through the API for this
    zone.
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
