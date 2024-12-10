# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .logging_param import LoggingParam

__all__ = [
    "RedirectRuleParam",
    "ActionParameters",
    "ActionParametersFromList",
    "ActionParametersFromValue",
    "ActionParametersFromValueTargetURL",
    "ActionParametersFromValueTargetURLStaticURLRedirect",
    "ActionParametersFromValueTargetURLDynamicURLRedirect",
    "ExposedCredentialCheck",
    "Ratelimit",
]


class ActionParametersFromList(TypedDict, total=False):
    key: str
    """Expression that evaluates to the list lookup key."""

    name: str
    """The name of the list to match against."""


class ActionParametersFromValueTargetURLStaticURLRedirect(TypedDict, total=False):
    value: str
    """The URL to redirect the request to."""


class ActionParametersFromValueTargetURLDynamicURLRedirect(TypedDict, total=False):
    expression: str
    """An expression to evaluate to get the URL to redirect the request to."""


ActionParametersFromValueTargetURL: TypeAlias = Union[
    ActionParametersFromValueTargetURLStaticURLRedirect, ActionParametersFromValueTargetURLDynamicURLRedirect
]


class ActionParametersFromValue(TypedDict, total=False):
    preserve_query_string: bool
    """Keep the query string of the original request."""

    status_code: Literal[301, 302, 303, 307, 308]
    """The status code to be used for the redirect."""

    target_url: ActionParametersFromValueTargetURL
    """The URL to redirect the request to."""


class ActionParameters(TypedDict, total=False):
    from_list: ActionParametersFromList
    """Serve a redirect based on a bulk list lookup."""

    from_value: ActionParametersFromValue
    """Serve a redirect based on the request properties."""


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
    """Configure checks for exposed credentials."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    ratelimit: Ratelimit
    """An object configuring the rule's ratelimit behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""
