# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .enforcement_rule import EnforcementRule

__all__ = ["PrecursorConfig"]


class PrecursorConfig(BaseModel):
    default_mode: Optional[Literal["off", "min-friction", "max-security"]] = None
    """
    The zone-level Precursor enforcement mode applied to requests that do not match
    a more specific enforcement rule.
    """

    enforcement_rules: Optional[List[EnforcementRule]] = None
    """The ordered list of enforcement rules for the zone."""
