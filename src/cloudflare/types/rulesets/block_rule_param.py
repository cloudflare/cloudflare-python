# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict, Required

from .logging_param import LoggingParam

__all__ = ["BlockRuleParam", "ActionParameters", "ActionParametersResponse"]


class ActionParametersResponse(TypedDict, total=False):
    content: Required[str]
    """The content to return."""

    content_type: Required[str]
    """The type of the content to return."""

    status_code: Required[int]
    """The status code to return."""


class ActionParameters(TypedDict, total=False):
    response: ActionParametersResponse
    """The response to show when the block is applied."""


class BlockRuleParam(TypedDict, total=False):
    id: str
    """The unique ID of the rule."""

    action: Literal["block"]
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
