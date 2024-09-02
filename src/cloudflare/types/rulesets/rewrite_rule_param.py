# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict, Required, TypeAlias

from .logging_param import LoggingParam

from typing import Dict, Union

from .rewrite_uri_part_param import RewriteURIPartParam

__all__ = [
    "RewriteRuleParam",
    "ActionParameters",
    "ActionParametersHeaders",
    "ActionParametersHeadersRemoveHeader",
    "ActionParametersHeadersStaticHeader",
    "ActionParametersHeadersDynamicHeader",
    "ActionParametersURI",
]


class ActionParametersHeadersRemoveHeader(TypedDict, total=False):
    operation: Required[Literal["remove"]]


class ActionParametersHeadersStaticHeader(TypedDict, total=False):
    operation: Required[Literal["set"]]

    value: Required[str]
    """Static value for the header."""


class ActionParametersHeadersDynamicHeader(TypedDict, total=False):
    expression: Required[str]
    """Expression for the header value."""

    operation: Required[Literal["set"]]


ActionParametersHeaders: TypeAlias = Union[
    ActionParametersHeadersRemoveHeader, ActionParametersHeadersStaticHeader, ActionParametersHeadersDynamicHeader
]


class ActionParametersURI(TypedDict, total=False):
    path: RewriteURIPartParam
    """Path portion rewrite."""

    query: RewriteURIPartParam
    """Query portion rewrite."""


class ActionParameters(TypedDict, total=False):
    headers: Dict[str, ActionParametersHeaders]
    """Map of request headers to modify."""

    uri: ActionParametersURI
    """URI to rewrite the request to."""


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

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""
