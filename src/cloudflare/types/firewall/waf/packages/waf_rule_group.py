# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["WAFRuleGroup"]


class WAFRuleGroup(BaseModel):
    id: Optional[str] = None
    """The unique identifier of the rule group."""

    name: Optional[str] = None
    """The name of the rule group."""
