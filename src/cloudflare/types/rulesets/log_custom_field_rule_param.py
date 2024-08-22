# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict, Required

from .logging_param import LoggingParam

from typing import Iterable

__all__ = ["LogCustomFieldRuleParam", "ActionParameters", "ActionParametersCookieField", "ActionParametersRequestField", "ActionParametersResponseField"]

class ActionParametersCookieField(TypedDict, total=False):
    name: Required[str]
    """The name of the field."""

class ActionParametersRequestField(TypedDict, total=False):
    name: Required[str]
    """The name of the field."""

class ActionParametersResponseField(TypedDict, total=False):
    name: Required[str]
    """The name of the field."""

class ActionParameters(TypedDict, total=False):
    cookie_fields: Iterable[ActionParametersCookieField]
    """The cookie fields to log."""

    request_fields: Iterable[ActionParametersRequestField]
    """The request fields to log."""

    response_fields: Iterable[ActionParametersResponseField]
    """The response fields to log."""

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

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""