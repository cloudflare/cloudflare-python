# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .logging_param import LoggingParam

__all__ = ["SetConfigRuleParam", "ActionParameters", "ActionParametersAutominify"]

class ActionParametersAutominify(TypedDict, total=False):
    css: bool
    """Minify CSS files."""

    html: bool
    """Minify HTML files."""

    js: bool
    """Minify JS files."""

class ActionParameters(TypedDict, total=False):
    automatic_https_rewrites: bool
    """Turn on or off Automatic HTTPS Rewrites."""

    autominify: ActionParametersAutominify
    """Select which file extensions to minify automatically."""

    bic: bool
    """Turn on or off Browser Integrity Check."""

    disable_apps: Literal[True]
    """Turn off all active Cloudflare Apps."""

    disable_rum: Literal[True]
    """Turn off Real User Monitoring (RUM)."""

    disable_zaraz: Literal[True]
    """Turn off Zaraz."""

    email_obfuscation: bool
    """Turn on or off Email Obfuscation."""

    fonts: bool
    """Turn on or off Cloudflare Fonts."""

    hotlink_protection: bool
    """Turn on or off the Hotlink Protection."""

    mirage: bool
    """Turn on or off Mirage."""

    opportunistic_encryption: bool
    """Turn on or off Opportunistic Encryption."""

    polish: Literal["off", "lossless", "lossy"]
    """Configure the Polish level."""

    rocket_loader: bool
    """Turn on or off Rocket Loader"""

    security_level: Literal["off", "essentially_off", "low", "medium", "high", "under_attack"]
    """Configure the Security Level."""

    server_side_excludes: bool
    """Turn on or off Server Side Excludes."""

    ssl: Literal["off", "flexible", "full", "strict", "origin_pull"]
    """Configure the SSL level."""

    sxg: bool
    """Turn on or off Signed Exchanges (SXG)."""

class SetConfigRuleParam(TypedDict, total=False):
    id: str
    """The unique ID of the rule."""

    action: Literal["set_config"]
    """The action to perform when the rule matches."""

    action_parameters: ActionParameters
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""