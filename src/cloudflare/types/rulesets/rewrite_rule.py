# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .logging import Logging
from ..._models import BaseModel
from .rewrite_uri_part import RewriteURIPart

__all__ = [
    "RewriteRule",
    "ActionParameters",
    "ActionParametersHeaders",
    "ActionParametersHeadersRemoveHeader",
    "ActionParametersHeadersStaticHeader",
    "ActionParametersHeadersDynamicHeader",
    "ActionParametersURI",
    "ExposedCredentialCheck",
    "Ratelimit",
]


class ActionParametersHeadersRemoveHeader(BaseModel):
    operation: Literal["remove"]


class ActionParametersHeadersStaticHeader(BaseModel):
    operation: Literal["set"]

    value: str
    """Static value for the header."""


class ActionParametersHeadersDynamicHeader(BaseModel):
    expression: str
    """Expression for the header value."""

    operation: Literal["set"]


ActionParametersHeaders: TypeAlias = Union[
    ActionParametersHeadersRemoveHeader, ActionParametersHeadersStaticHeader, ActionParametersHeadersDynamicHeader
]


class ActionParametersURI(BaseModel):
    path: Optional[RewriteURIPart] = None
    """Path portion rewrite."""

    query: Optional[RewriteURIPart] = None
    """Query portion rewrite."""


class ActionParameters(BaseModel):
    headers: Optional[Dict[str, ActionParametersHeaders]] = None
    """Map of request headers to modify."""

    uri: Optional[ActionParametersURI] = None
    """URI to rewrite the request to."""


class ExposedCredentialCheck(BaseModel):
    password_expression: str
    """Expression that selects the password used in the credentials check."""

    username_expression: str
    """Expression that selects the user ID used in the credentials check."""


class Ratelimit(BaseModel):
    characteristics: List[str]
    """
    Characteristics of the request on which the ratelimiter counter will be
    incremented.
    """

    period: Literal[10, 60, 600, 3600]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: Optional[str] = None
    """Defines when the ratelimit counter should be incremented.

    It is optional and defaults to the same as the rule's expression.
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
    """Defines if ratelimit counting is only done when an origin is reached."""

    score_per_period: Optional[int] = None
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: Optional[str] = None
    """
    The response header name provided by the origin which should contain the score
    to increment ratelimit counter on.
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
    """Configure checks for exposed credentials."""

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[Ratelimit] = None
    """An object configuring the rule's ratelimit behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule ID by default)."""
