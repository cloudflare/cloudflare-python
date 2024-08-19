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

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule ID by default)."""
