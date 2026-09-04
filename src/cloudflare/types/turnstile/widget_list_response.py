# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .widget_domain import WidgetDomain

__all__ = ["WidgetListResponse"]


class WidgetListResponse(BaseModel):
    """A Turnstile Widgets configuration as it appears in listings"""

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

    region: Literal["world", "china"]
    """Region where this widget can be used. This cannot be changed after creation."""

    sitekey: str
    """Widget item identifier tag."""

    deployed_via: Optional[Literal["wrangler", "dashboard", "spin", "api", "unknown"]] = None
    """
    Origin that created this widget, recorded at creation time and immutable
    afterward. Server-derived from the create request; not client-settable. Omitted
    from the response for widgets created before this field existed.
    """

    last_modified_via: Optional[Literal["wrangler", "dashboard", "spin", "api", "unknown"]] = None
    """Origin of the most recent mutation (create, update, delete, or secret rotation).

    Server-derived; not client-settable. Omitted for widgets last mutated before
    this field existed.
    """
