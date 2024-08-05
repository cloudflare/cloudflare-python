# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .logging import Logging
from ..._models import BaseModel
from .rewrite_uri_part import RewriteURIPart

__all__ = [
    "RewriteRule",
    "ActionParameters",
    "ActionParametersHeaders",
    "ActionParametersHeadersRemoveHeader",
    "ActionParametersHeadersStaticHeader",
    "ActionParametersHeadersDynamicHeader",
    "ActionParametersURI",
]


class ActionParametersHeadersRemoveHeader(BaseModel):
    operation: Literal["remove"]


class ActionParametersHeadersStaticHeader(BaseModel):
    operation: Literal["set"]

    value: str
    """Static value for the header."""


class ActionParametersHeadersDynamicHeader(BaseModel):
    expression: str
    """Expression for the header value."""

    operation: Literal["set"]


ActionParametersHeaders: TypeAlias = Union[
    ActionParametersHeadersRemoveHeader, ActionParametersHeadersStaticHeader, ActionParametersHeadersDynamicHeader
]


class ActionParametersURI(BaseModel):
    path: Optional[RewriteURIPart] = None
    """Path portion rewrite."""

    query: Optional[RewriteURIPart] = None
    """Query portion rewrite."""


class ActionParameters(BaseModel):
    headers: Optional[Dict[str, ActionParametersHeaders]] = None
    """Map of request headers to modify."""

    uri: Optional[ActionParametersURI] = None
    """URI to rewrite the request to."""


class RewriteRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["rewrite"]] = None
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
