# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .logging import Logging
from ..._models import BaseModel

__all__ = [
    "RewriteRule",
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


class ActionParametersHeadersAddStaticHeader(BaseModel):
    """A header with a static value to add."""

    operation: Literal["add"]
    """The operation to perform on the header."""

    value: str
    """A static value for the header."""


class ActionParametersHeadersAddDynamicHeader(BaseModel):
    """A header with a dynamic value to add."""

    expression: str
    """An expression that evaluates to a value for the header."""

    operation: Literal["add"]
    """The operation to perform on the header."""


class ActionParametersHeadersSetStaticHeader(BaseModel):
    """A header with a static value to set."""

    operation: Literal["set"]
    """The operation to perform on the header."""

    value: str
    """A static value for the header."""


class ActionParametersHeadersSetDynamicHeader(BaseModel):
    """A header with a dynamic value to set."""

    expression: str
    """An expression that evaluates to a value for the header."""

    operation: Literal["set"]
    """The operation to perform on the header."""


class ActionParametersHeadersRemoveHeader(BaseModel):
    """A header to remove."""

    operation: Literal["remove"]
    """The operation to perform on the header."""


ActionParametersHeaders: TypeAlias = Union[
    ActionParametersHeadersAddStaticHeader,
    ActionParametersHeadersAddDynamicHeader,
    ActionParametersHeadersSetStaticHeader,
    ActionParametersHeadersSetDynamicHeader,
    ActionParametersHeadersRemoveHeader,
]


class ActionParametersURIURIPathPath(BaseModel):
    """A URI path rewrite."""

    expression: Optional[str] = None
    """An expression that evaluates to a value to rewrite the URI path to."""

    value: Optional[str] = None
    """A value to rewrite the URI path to."""


class ActionParametersURIURIPath(BaseModel):
    """A URI path rewrite."""

    path: ActionParametersURIURIPathPath
    """A URI path rewrite."""

    origin: Optional[bool] = None
    """Whether to propagate the rewritten URI to origin."""


class ActionParametersURIURIQueryQuery(BaseModel):
    """A URI query rewrite."""

    expression: Optional[str] = None
    """An expression that evaluates to a value to rewrite the URI query to."""

    value: Optional[str] = None
    """A value to rewrite the URI query to."""


class ActionParametersURIURIQuery(BaseModel):
    """A URI query rewrite."""

    query: ActionParametersURIURIQueryQuery
    """A URI query rewrite."""

    origin: Optional[bool] = None
    """Whether to propagate the rewritten URI to origin."""


ActionParametersURI: TypeAlias = Union[ActionParametersURIURIPath, ActionParametersURIURIQuery]


class ActionParameters(BaseModel):
    """The parameters configuring the rule's action."""

    headers: Optional[Dict[str, ActionParametersHeaders]] = None
    """A map of headers to rewrite."""

    uri: Optional[ActionParametersURI] = None
    """A URI path rewrite."""


class ExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class Ratelimit(BaseModel):
    """An object configuring the rule's rate limit behavior."""

    characteristics: List[str]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: int
    """Period in seconds over which the counter is being incremented."""

    counting_expression: Optional[str] = None
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
    """

    mitigation_timeout: Optional[int] = None
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: Optional[int] = None
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: Optional[bool] = None
    """Whether counting is only performed when an origin is reached."""

    score_per_period: Optional[int] = None
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: Optional[str] = None
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
    """


class RewriteRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["rewrite"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[ActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    enabled: Optional[bool] = None
    """Whether the rule should be executed."""

    exposed_credential_check: Optional[ExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[Ratelimit] = None
    """An object configuring the rule's rate limit behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule's ID by default)."""
