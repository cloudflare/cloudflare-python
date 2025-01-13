# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .widget_domain import WidgetDomain

__all__ = ["WidgetListResponse"]


class WidgetListResponse(BaseModel):
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

    created_on: datetime
    """When the widget was created."""

    domains: List[WidgetDomain]

    ephemeral_id: bool
    """Return the Ephemeral ID in /siteverify (ENT only)."""

    mode: Literal["non-interactive", "invisible", "managed"]
    """Widget Mode"""

    modified_on: datetime
    """When the widget was modified."""

    name: str
    """Human readable widget name.

    Not unique. Cloudflare suggests that you set this to a meaningful string to make
    it easier to identify your widget, and where it is used.
    """

    offlabel: bool
    """Do not show any Cloudflare branding on the widget (ENT only)."""

    region: Literal["world"]
    """Region where this widget can be used."""

    sitekey: str
    """Widget item identifier tag."""
