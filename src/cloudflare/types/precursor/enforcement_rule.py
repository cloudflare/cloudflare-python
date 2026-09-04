# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["EnforcementRule"]


class EnforcementRule(BaseModel):
    expression: str
    """The filter expression that determines which requests the rule matches."""

    mode: Literal["min-friction", "max-security"]
    """The override mode Precursor applies to requests matching an enforcement rule.

    Unlike `default_mode`, this cannot be `off`.
    """

    id: Optional[str] = None
    """The read-only identifier that Cloudflare assigns to the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    enabled: Optional[bool] = None
    """Whether the rule is active."""
