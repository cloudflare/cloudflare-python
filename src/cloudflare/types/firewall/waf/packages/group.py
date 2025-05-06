# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["Group"]


class Group(BaseModel):
    id: str
    """Defines the unique identifier of the rule group."""

    description: Optional[str] = None
    """Defines an informative summary of what the rule group does."""

    mode: Literal["on", "off"]
    """Defines the state of the rules contained in the rule group.

    When `on`, the rules in the group are configurable/usable.
    """

    name: str
    """Defines the name of the rule group."""

    rules_count: float
    """Defines the number of rules in the current rule group."""

    allowed_modes: Optional[List[Literal["on", "off"]]] = None
    """Defines the available states for the rule group."""

    modified_rules_count: Optional[float] = None
    """
    Defines the number of rules within the group that have been modified from their
    default configuration.
    """

    package_id: Optional[str] = None
    """Defines the unique identifier of a WAF package."""
