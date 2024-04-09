# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .rum_rule import RUMRule
from ..._models import BaseModel

__all__ = ["Site", "Ruleset"]


class Ruleset(BaseModel):
    id: Optional[str] = None
    """The Web Analytics ruleset identifier."""

    enabled: Optional[bool] = None
    """Whether the ruleset is enabled."""

    zone_name: Optional[str] = None

    zone_tag: Optional[str] = None
    """The zone identifier."""


class Site(BaseModel):
    auto_install: Optional[bool] = None
    """
    If enabled, the JavaScript snippet is automatically injected for orange-clouded
    sites.
    """

    created: Optional[datetime] = None

    rules: Optional[List[RUMRule]] = None
    """A list of rules."""

    ruleset: Optional[Ruleset] = None

    site_tag: Optional[str] = None
    """The Web Analytics site identifier."""

    site_token: Optional[str] = None
    """The Web Analytics site token."""

    snippet: Optional[str] = None
    """Encoded JavaScript snippet."""
