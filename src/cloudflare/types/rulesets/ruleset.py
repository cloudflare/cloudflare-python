# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .kind import Kind
from .phase import Phase
from ..._models import BaseModel

__all__ = ["Ruleset"]


class Ruleset(BaseModel):
    id: str
    """The unique ID of the ruleset."""

    last_updated: datetime
    """The timestamp of when the ruleset was last modified."""

    version: str
    """The version of the ruleset."""

    description: Optional[str] = None
    """An informative description of the ruleset."""

    kind: Optional[Kind] = None
    """The kind of the ruleset."""

    name: Optional[str] = None
    """The human-readable name of the ruleset."""

    phase: Optional[Phase] = None
    """The phase of the ruleset."""
