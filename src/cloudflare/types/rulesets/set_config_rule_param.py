# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

from .logging_param import LoggingParam

__all__ = [
    "SetConfigRuleParam",
    "ActionParameters",
    "ActionParametersAutominify",
    "ExposedCredentialCheck",
    "Ratelimit",
]


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


class ExposedCredentialCheck(TypedDict, total=False):
    password_expression: Required[str]
    """Expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """Expression that selects the user ID used in the credentials check."""


class Ratelimit(TypedDict, total=False):
    characteristics: Required[List[str]]
    """
    Characteristics of the request on which the ratelimiter counter will be
    incremented.
    """

    period: Required[Literal[10, 60, 600, 3600]]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """Defines when the ratelimit counter should be incremented.

    It is optional and defaults to the same as the rule's expression.
    """

    mitigation_timeout: int
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: int
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: bool
    """Defines if ratelimit counting is only done when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    The response header name provided by the origin which should contain the score
    to increment ratelimit counter on.
    """


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

    exposed_credential_check: ExposedCredentialCheck
    """Configure checks for exposed credentials."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    ratelimit: Ratelimit
    """An object configuring the rule's ratelimit behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""
