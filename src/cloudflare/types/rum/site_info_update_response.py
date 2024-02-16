# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["SiteInfoUpdateResponse", "Rule", "Ruleset"]


class Rule(BaseModel):
    id: Optional[str] = None
    """The Web Analytics rule identifier."""

    created: Optional[datetime] = None

    host: Optional[str] = None
    """The hostname the rule will be applied to."""

    inclusive: Optional[bool] = None
    """Whether the rule includes or excludes traffic from being measured."""

    is_paused: Optional[bool] = None
    """Whether the rule is paused or not."""

    paths: Optional[List[str]] = None
    """The paths the rule will be applied to."""

    priority: Optional[float] = None


class Ruleset(BaseModel):
    id: Optional[str] = None
    """The Web Analytics ruleset identifier."""

    enabled: Optional[bool] = None
    """Whether the ruleset is enabled."""

    zone_name: Optional[str] = None

    zone_tag: Optional[str] = None
    """The zone identifier."""


class SiteInfoUpdateResponse(BaseModel):
    auto_install: Optional[bool] = None
    """
    If enabled, the JavaScript snippet is automatically injected for orange-clouded
    sites.
    """

    created: Optional[datetime] = None

    rules: Optional[List[Rule]] = None
    """A list of rules."""

    ruleset: Optional[Ruleset] = None

    site_tag: Optional[str] = None
    """The Web Analytics site identifier."""

    site_token: Optional[str] = None
    """The Web Analytics site token."""

    snippet: Optional[str] = None
    """Encoded JavaScript snippet."""
