# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .logging_param import LoggingParam

__all__ = [
    "RewriteRuleParam",
    "ActionParameters",
    "ActionParametersHeaders",
    "ActionParametersHeadersAddStaticHeader",
    "ActionParametersHeadersAddDynamicHeader",
    "ActionParametersHeadersSetStaticHeader",
    "ActionParametersHeadersSetDynamicHeader",
    "ActionParametersHeadersRemoveHeader",
    "ActionParametersURI",
    "ActionParametersURIURIPath",
    "ActionParametersURIURIPathPath",
    "ActionParametersURIURIQuery",
    "ActionParametersURIURIQueryQuery",
    "ExposedCredentialCheck",
    "Ratelimit",
]


class ActionParametersHeadersAddStaticHeader(TypedDict, total=False):
    operation: Required[Literal["add"]]
    """The operation to perform on the header."""

    value: Required[str]
    """A static value for the header."""


class ActionParametersHeadersAddDynamicHeader(TypedDict, total=False):
    expression: Required[str]
    """An expression that evaluates to a value for the header."""

    operation: Required[Literal["add"]]
    """The operation to perform on the header."""


class ActionParametersHeadersSetStaticHeader(TypedDict, total=False):
    operation: Required[Literal["set"]]
    """The operation to perform on the header."""

    value: Required[str]
    """A static value for the header."""


class ActionParametersHeadersSetDynamicHeader(TypedDict, total=False):
    expression: Required[str]
    """An expression that evaluates to a value for the header."""

    operation: Required[Literal["set"]]
    """The operation to perform on the header."""


class ActionParametersHeadersRemoveHeader(TypedDict, total=False):
    operation: Required[Literal["remove"]]
    """The operation to perform on the header."""


ActionParametersHeaders: TypeAlias = Union[
    ActionParametersHeadersAddStaticHeader,
    ActionParametersHeadersAddDynamicHeader,
    ActionParametersHeadersSetStaticHeader,
    ActionParametersHeadersSetDynamicHeader,
    ActionParametersHeadersRemoveHeader,
]


class ActionParametersURIURIPathPath(TypedDict, total=False):
    expression: str
    """An expression that evaluates to a value to rewrite the URI path to."""

    value: str
    """A value to rewrite the URI path to."""


class ActionParametersURIURIPath(TypedDict, total=False):
    path: Required[ActionParametersURIURIPathPath]
    """A URI path rewrite."""


class ActionParametersURIURIQueryQuery(TypedDict, total=False):
    expression: str
    """An expression that evaluates to a value to rewrite the URI query to."""

    value: str
    """A value to rewrite the URI query to."""


class ActionParametersURIURIQuery(TypedDict, total=False):
    query: Required[ActionParametersURIURIQueryQuery]
    """A URI query rewrite."""


ActionParametersURI: TypeAlias = Union[ActionParametersURIURIPath, ActionParametersURIURIQuery]


class ActionParameters(TypedDict, total=False):
    headers: Dict[str, ActionParametersHeaders]
    """A map of headers to rewrite."""

    uri: ActionParametersURI
    """A URI path rewrite."""


class ExposedCredentialCheck(TypedDict, total=False):
    password_expression: Required[str]
    """An expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """An expression that selects the user ID used in the credentials check."""


class Ratelimit(TypedDict, total=False):
    characteristics: Required[List[str]]
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
    """Configuration for exposed credential checking."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    ratelimit: Ratelimit
    """An object configuring the rule's rate limit behavior."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""
