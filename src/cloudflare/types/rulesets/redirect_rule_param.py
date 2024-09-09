# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypeAlias, TypedDict

from .logging_param import LoggingParam

__all__ = [
    "RedirectRuleParam",
    "ActionParameters",
    "ActionParametersFromList",
    "ActionParametersFromValue",
    "ActionParametersFromValueTargetURL",
    "ActionParametersFromValueTargetURLStaticURLRedirect",
    "ActionParametersFromValueTargetURLDynamicURLRedirect",
]


class ActionParametersFromList(TypedDict, total=False):
    key: str
    """Expression that evaluates to the list lookup key."""

    name: str
    """The name of the list to match against."""


class ActionParametersFromValueTargetURLStaticURLRedirect(TypedDict, total=False):
    value: str
    """The URL to redirect the request to."""


class ActionParametersFromValueTargetURLDynamicURLRedirect(TypedDict, total=False):
    expression: str
    """An expression to evaluate to get the URL to redirect the request to."""


ActionParametersFromValueTargetURL: TypeAlias = Union[
    ActionParametersFromValueTargetURLStaticURLRedirect, ActionParametersFromValueTargetURLDynamicURLRedirect
]


class ActionParametersFromValue(TypedDict, total=False):
    preserve_query_string: bool
    """Keep the query string of the original request."""

    status_code: Literal[301, 302, 303, 307, 308]
    """The status code to be used for the redirect."""

    target_url: ActionParametersFromValueTargetURL
    """The URL to redirect the request to."""


class ActionParameters(TypedDict, total=False):
    from_list: ActionParametersFromList
    """Serve a redirect based on a bulk list lookup."""

    from_value: ActionParametersFromValue
    """Serve a redirect based on the request properties."""


class RedirectRuleParam(TypedDict, total=False):
    id: str
    """The unique ID of the rule."""

    action: Literal["redirect"]
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
