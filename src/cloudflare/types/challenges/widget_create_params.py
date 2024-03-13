# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WidgetCreateParams"]


class WidgetCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    domains: Required[List[str]]

    mode: Required[Literal["non-interactive", "invisible", "managed"]]
    """Widget Mode"""

    name: Required[str]
    """Human readable widget name.

    Not unique. Cloudflare suggests that you set this to a meaningful string to make
    it easier to identify your widget, and where it is used.
    """

    direction: Literal["asc", "desc"]
    """Direction to order widgets."""

    order: Literal["id", "sitekey", "name", "created_on", "modified_on"]
    """Field to order widgets by."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of items per page."""

    bot_fight_mode: bool
    """
    If bot_fight_mode is set to `true`, Cloudflare issues computationally expensive
    challenges in response to malicious bots (ENT only).
    """

    clearance_level: Literal["no_clearance", "jschallenge", "managed", "interactive"]
    """
    If Turnstile is embedded on a Cloudflare site and the widget should grant
    challenge clearance, this setting can determine the clearance level to be set
    """

    offlabel: bool
    """Do not show any Cloudflare branding on the widget (ENT only)."""

    region: Literal["world"]
    """Region where this widget can be used."""
