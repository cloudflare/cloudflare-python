# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .logging import Logging
from ..._models import BaseModel

__all__ = [
    "RedirectRule",
    "ActionParameters",
    "ActionParametersFromList",
    "ActionParametersFromValue",
    "ActionParametersFromValueTargetURL",
    "ActionParametersFromValueTargetURLStaticURLRedirect",
    "ActionParametersFromValueTargetURLDynamicURLRedirect",
    "ExposedCredentialCheck",
    "Ratelimit",
]


class ActionParametersFromList(BaseModel):
    key: Optional[str] = None
    """Expression that evaluates to the list lookup key."""

    name: Optional[str] = None
    """The name of the list to match against."""


class ActionParametersFromValueTargetURLStaticURLRedirect(BaseModel):
    value: Optional[str] = None
    """The URL to redirect the request to."""


class ActionParametersFromValueTargetURLDynamicURLRedirect(BaseModel):
    expression: Optional[str] = None
    """An expression to evaluate to get the URL to redirect the request to."""


ActionParametersFromValueTargetURL: TypeAlias = Union[
    ActionParametersFromValueTargetURLStaticURLRedirect, ActionParametersFromValueTargetURLDynamicURLRedirect
]


class ActionParametersFromValue(BaseModel):
    preserve_query_string: Optional[bool] = None
    """Keep the query string of the original request."""

    status_code: Optional[Literal[301, 302, 303, 307, 308]] = None
    """The status code to be used for the redirect."""

    target_url: Optional[ActionParametersFromValueTargetURL] = None
    """The URL to redirect the request to."""


class ActionParameters(BaseModel):
    from_list: Optional[ActionParametersFromList] = None
    """Serve a redirect based on a bulk list lookup."""

    from_value: Optional[ActionParametersFromValue] = None
    """Serve a redirect based on the request properties."""


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


class RedirectRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["redirect"]] = None
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
