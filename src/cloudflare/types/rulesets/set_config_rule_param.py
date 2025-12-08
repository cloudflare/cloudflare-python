# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr
from .logging_param import LoggingParam

__all__ = [
    "SetConfigRuleParam",
    "ActionParameters",
    "ActionParametersAutominify",
    "ExposedCredentialCheck",
    "Ratelimit",
]


class ActionParametersAutominify(TypedDict, total=False):
    """Which file extensions to minify automatically."""

    css: bool
    """Whether to minify CSS files."""

    html: bool
    """Whether to minify HTML files."""

    js: bool
    """Whether to minify JavaScript files."""


class ActionParameters(TypedDict, total=False):
    """The parameters configuring the rule's action."""

    automatic_https_rewrites: bool
    """Whether to enable Automatic HTTPS Rewrites."""

    autominify: ActionParametersAutominify
    """Which file extensions to minify automatically."""

    bic: bool
    """Whether to enable Browser Integrity Check (BIC)."""

    disable_apps: Literal[True]
    """Whether to disable Cloudflare Apps."""

    disable_pay_per_crawl: Literal[True]
    """Whether to disable Pay Per Crawl."""

    disable_rum: Literal[True]
    """Whether to disable Real User Monitoring (RUM)."""

    disable_zaraz: Literal[True]
    """Whether to disable Zaraz."""

    email_obfuscation: bool
    """Whether to enable Email Obfuscation."""

    fonts: bool
    """Whether to enable Cloudflare Fonts."""

    hotlink_protection: bool
    """Whether to enable Hotlink Protection."""

    mirage: bool
    """Whether to enable Mirage."""

    opportunistic_encryption: bool
    """Whether to enable Opportunistic Encryption."""

    polish: Literal["off", "lossless", "lossy", "webp"]
    """The Polish level to configure."""

    rocket_loader: bool
    """Whether to enable Rocket Loader."""

    security_level: Literal["off", "essentially_off", "low", "medium", "high", "under_attack"]
    """The Security Level to configure."""

    server_side_excludes: bool
    """Whether to enable Server-Side Excludes."""

    ssl: Literal["off", "flexible", "full", "strict", "origin_pull"]
    """The SSL level to configure."""

    sxg: bool
    """Whether to enable Signed Exchanges (SXG)."""


class ExposedCredentialCheck(TypedDict, total=False):
    """Configuration for exposed credential checking."""

    password_expression: Required[str]
    """An expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """An expression that selects the user ID used in the credentials check."""


class Ratelimit(TypedDict, total=False):
    """An object configuring the rule's rate limit behavior."""

    characteristics: Required[SequenceNotStr[str]]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: Required[int]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
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
    """Whether counting is only performed when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
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
    """Configuration for exposed credential checking."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    ratelimit: Ratelimit
    """An object configuring the rule's rate limit behavior."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""
