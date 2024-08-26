# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict, Required

from .logging_param import LoggingParam

__all__ = ["RouteRuleParam", "ActionParameters", "ActionParametersOrigin", "ActionParametersSNI"]

class ActionParametersOrigin(TypedDict, total=False):
    host: str
    """Override the resolved hostname."""

    port: float
    """Override the destination port."""

class ActionParametersSNI(TypedDict, total=False):
    value: Required[str]
    """The SNI override."""

class ActionParameters(TypedDict, total=False):
    host_header: str
    """Rewrite the HTTP Host header."""

    origin: ActionParametersOrigin
    """Override the IP/TCP destination."""

    sni: ActionParametersSNI
    """Override the Server Name Indication (SNI)."""

class RouteRuleParam(TypedDict, total=False):
    id: str
    """The unique ID of the rule."""

    action: Literal["route"]
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