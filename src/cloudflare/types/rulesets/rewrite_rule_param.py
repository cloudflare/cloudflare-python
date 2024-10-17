# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .logging_param import LoggingParam
from .rewrite_uri_part_param import RewriteURIPartParam

__all__ = [
    "RewriteRuleParam",
    "ActionParameters",
    "ActionParametersHeaders",
    "ActionParametersHeadersRemoveHeader",
    "ActionParametersHeadersStaticHeader",
    "ActionParametersHeadersDynamicHeader",
    "ActionParametersURI",
    "ExposedCredentialCheck",
    "Ratelimit",
]


class ActionParametersHeadersRemoveHeader(TypedDict, total=False):
    operation: Required[Literal["remove"]]


class ActionParametersHeadersStaticHeader(TypedDict, total=False):
    operation: Required[Literal["set"]]

    value: Required[str]
    """Static value for the header."""


class ActionParametersHeadersDynamicHeader(TypedDict, total=False):
    expression: Required[str]
    """Expression for the header value."""

    operation: Required[Literal["set"]]


ActionParametersHeaders: TypeAlias = Union[
    ActionParametersHeadersRemoveHeader, ActionParametersHeadersStaticHeader, ActionParametersHeadersDynamicHeader
]


class ActionParametersURI(TypedDict, total=False):
    path: RewriteURIPartParam
    """Path portion rewrite."""

    query: RewriteURIPartParam
    """Query portion rewrite."""


class ActionParameters(TypedDict, total=False):
    headers: Dict[str, ActionParametersHeaders]
    """Map of request headers to modify."""

    uri: ActionParametersURI
    """URI to rewrite the request to."""


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


class RewriteRuleParam(TypedDict, total=False):
    id: str
    """The unique ID of the rule."""

    action: Literal["rewrite"]
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
