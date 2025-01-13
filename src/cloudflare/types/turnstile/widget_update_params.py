# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

from .widget_domain import WidgetDomain

__all__ = ["WidgetUpdateParams"]


class WidgetUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    domains: Required[List[WidgetDomain]]

    mode: Required[Literal["non-interactive", "invisible", "managed"]]
    """Widget Mode"""

    name: Required[str]
    """Human readable widget name.

    Not unique. Cloudflare suggests that you set this to a meaningful string to make
    it easier to identify your widget, and where it is used.
    """

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

    ephemeral_id: bool
    """Return the Ephemeral ID in /siteverify (ENT only)."""

    offlabel: bool
    """Do not show any Cloudflare branding on the widget (ENT only)."""
