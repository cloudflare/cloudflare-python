# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .logging import Logging
from ..._models import BaseModel

__all__ = ["RouteRule", "ActionParameters", "ActionParametersOrigin", "ActionParametersSNI"]


class ActionParametersOrigin(BaseModel):
    host: Optional[str] = None
    """Override the resolved hostname."""

    port: Optional[float] = None
    """Override the destination port."""


class ActionParametersSNI(BaseModel):
    value: str
    """The SNI override."""


class ActionParameters(BaseModel):
    host_header: Optional[str] = None
    """Rewrite the HTTP Host header."""

    origin: Optional[ActionParametersOrigin] = None
    """Override the IP/TCP destination."""

    sni: Optional[ActionParametersSNI] = None
    """Override the Server Name Indication (SNI)."""


class RouteRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["route"]] = None
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
