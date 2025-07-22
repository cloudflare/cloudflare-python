# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["RuleDeleteResponse"]


class RuleDeleteResponse(BaseModel):
    id: str
    """The unique ID of the rule."""

    expression: str
    """The expression defining which traffic will match the rule."""

    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    snippet_name: str
    """The identifying name of the snippet."""

    description: Optional[str] = None
    """An informative description of the rule."""

    enabled: Optional[bool] = None
    """Whether the rule should be executed."""
