# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from .logging_param import LoggingParam

__all__ = [
    "ServeErrorRuleParam",
    "ActionParameters",
    "ActionParametersActionParametersContent",
    "ActionParametersActionParametersAsset",
    "ExposedCredentialCheck",
    "Ratelimit",
]


class ActionParametersActionParametersContent(TypedDict, total=False):
    content: Required[str]
    """The response content."""

    content_type: Literal["application/json", "text/html", "text/plain", "text/xml"]
    """The content type header to set with the error response."""

    status_code: int
    """The status code to use for the error."""


class ActionParametersActionParametersAsset(TypedDict, total=False):
    asset_name: Required[str]
    """The name of a custom asset to serve as the error response."""

    content_type: Literal["application/json", "text/html", "text/plain", "text/xml"]
    """The content type header to set with the error response."""

    status_code: int
    """The status code to use for the error."""


ActionParameters: TypeAlias = Union[ActionParametersActionParametersContent, ActionParametersActionParametersAsset]


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


class ServeErrorRuleParam(TypedDict, total=False):
    id: str
    """The unique ID of the rule."""

    action: Literal["serve_error"]
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
