# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .logging import Logging
from ..._models import BaseModel

__all__ = ["SetConfigRule", "ActionParameters", "ActionParametersAutominify"]


class ActionParametersAutominify(BaseModel):
    css: Optional[bool] = None
    """Minify CSS files."""

    html: Optional[bool] = None
    """Minify HTML files."""

    js: Optional[bool] = None
    """Minify JS files."""


class ActionParameters(BaseModel):
    automatic_https_rewrites: Optional[bool] = None
    """Turn on or off Automatic HTTPS Rewrites."""

    autominify: Optional[ActionParametersAutominify] = None
    """Select which file extensions to minify automatically."""

    bic: Optional[bool] = None
    """Turn on or off Browser Integrity Check."""

    disable_apps: Optional[Literal[True]] = None
    """Turn off all active Cloudflare Apps."""

    disable_rum: Optional[Literal[True]] = None
    """Turn off Real User Monitoring (RUM)."""

    disable_zaraz: Optional[Literal[True]] = None
    """Turn off Zaraz."""

    email_obfuscation: Optional[bool] = None
    """Turn on or off Email Obfuscation."""

    fonts: Optional[bool] = None
    """Turn on or off Cloudflare Fonts."""

    hotlink_protection: Optional[bool] = None
    """Turn on or off the Hotlink Protection."""

    mirage: Optional[bool] = None
    """Turn on or off Mirage."""

    opportunistic_encryption: Optional[bool] = None
    """Turn on or off Opportunistic Encryption."""

    polish: Optional[Literal["off", "lossless", "lossy"]] = None
    """Configure the Polish level."""

    rocket_loader: Optional[bool] = None
    """Turn on or off Rocket Loader"""

    security_level: Optional[Literal["off", "essentially_off", "low", "medium", "high", "under_attack"]] = None
    """Configure the Security Level."""

    server_side_excludes: Optional[bool] = None
    """Turn on or off Server Side Excludes."""

    ssl: Optional[Literal["off", "flexible", "full", "strict", "origin_pull"]] = None
    """Configure the SSL level."""

    sxg: Optional[bool] = None
    """Turn on or off Signed Exchanges (SXG)."""


class SetConfigRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["set_config"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[ActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    enabled: Optional[bool] = None
    """Whether the rule should be executed."""

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule ID by default)."""
