# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

from .logging_param import LoggingParam

__all__ = [
    "LogCustomFieldRuleParam",
    "ActionParameters",
    "ActionParametersCookieField",
    "ActionParametersRawResponseField",
    "ActionParametersRequestField",
    "ActionParametersResponseField",
    "ActionParametersTransformedRequestField",
    "ExposedCredentialCheck",
    "Ratelimit",
]


class ActionParametersCookieField(TypedDict, total=False):
    name: Required[str]
    """The name of the field."""


class ActionParametersRawResponseField(TypedDict, total=False):
    name: Required[str]
    """The name of the field."""

    preserve_duplicates: bool
    """Whether to log duplicate values of the same header."""


class ActionParametersRequestField(TypedDict, total=False):
    name: Required[str]
    """The name of the field."""


class ActionParametersResponseField(TypedDict, total=False):
    name: Required[str]
    """The name of the field."""

    preserve_duplicates: bool
    """Whether to log duplicate values of the same header."""


class ActionParametersTransformedRequestField(TypedDict, total=False):
    name: Required[str]
    """The name of the field."""


class ActionParameters(TypedDict, total=False):
    cookie_fields: Iterable[ActionParametersCookieField]
    """The cookie fields to log."""

    raw_response_fields: Iterable[ActionParametersRawResponseField]
    """The raw response fields to log."""

    request_fields: Iterable[ActionParametersRequestField]
    """The raw request fields to log."""

    response_fields: Iterable[ActionParametersResponseField]
    """The transformed response fields to log."""

    transformed_request_fields: Iterable[ActionParametersTransformedRequestField]
    """The transformed request fields to log."""


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


class LogCustomFieldRuleParam(TypedDict, total=False):
    id: str
    """The unique ID of the rule."""

    action: Literal["log_custom_field"]
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
