# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from ..types import shared_params

__all__ = ["LogRuleParam"]


class LogRuleParam(TypedDict, total=False):
    id: str
    """The unique ID of the rule."""

    action: Literal["log"]
    """The action to perform when the rule matches."""

    action_parameters: object
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: shared_params.UnnamedSchemaRef70f2c6ccd8a405358ac7ef8fc3d6751c
    """An object configuring the rule's logging behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""
