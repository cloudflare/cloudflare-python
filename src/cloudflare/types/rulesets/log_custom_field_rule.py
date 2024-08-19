# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .logging import Logging
from ..._models import BaseModel

__all__ = [
    "LogCustomFieldRule",
    "ActionParameters",
    "ActionParametersCookieField",
    "ActionParametersRequestField",
    "ActionParametersResponseField",
]


class ActionParametersCookieField(BaseModel):
    name: str
    """The name of the field."""


class ActionParametersRequestField(BaseModel):
    name: str
    """The name of the field."""


class ActionParametersResponseField(BaseModel):
    name: str
    """The name of the field."""


class ActionParameters(BaseModel):
    cookie_fields: Optional[List[ActionParametersCookieField]] = None
    """The cookie fields to log."""

    request_fields: Optional[List[ActionParametersRequestField]] = None
    """The request fields to log."""

    response_fields: Optional[List[ActionParametersResponseField]] = None
    """The response fields to log."""


class LogCustomFieldRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["log_custom_field"]] = None
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
