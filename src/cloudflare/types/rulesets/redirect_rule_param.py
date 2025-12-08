# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr
from .logging_param import LoggingParam

__all__ = [
    "RedirectRuleParam",
    "ActionParameters",
    "ActionParametersFromList",
    "ActionParametersFromValue",
    "ActionParametersFromValueTargetURL",
    "ExposedCredentialCheck",
    "Ratelimit",
]


class ActionParametersFromList(TypedDict, total=False):
    """A redirect based on a bulk list lookup."""

    key: Required[str]
    """An expression that evaluates to the list lookup key."""

    name: Required[str]
    """The name of the list to match against."""


class ActionParametersFromValueTargetURL(TypedDict, total=False):
    """A URL to redirect the request to."""

    expression: str
    """An expression that evaluates to a URL to redirect the request to."""

    value: str
    """A URL to redirect the request to."""


class ActionParametersFromValue(TypedDict, total=False):
    """A redirect based on the request properties."""

    target_url: Required[ActionParametersFromValueTargetURL]
    """A URL to redirect the request to."""

    preserve_query_string: bool
    """Whether to keep the query string of the original request."""

    status_code: Literal[301, 302, 303, 307, 308]
    """The status code to use for the redirect."""


class ActionParameters(TypedDict, total=False):
    """The parameters configuring the rule's action."""

    from_list: ActionParametersFromList
    """A redirect based on a bulk list lookup."""

    from_value: ActionParametersFromValue
    """A redirect based on the request properties."""


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


class RedirectRuleParam(TypedDict, total=False):
    id: str
    """The unique ID of the rule."""

    action: Literal["redirect"]
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
