# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .action import Action
from .matcher import Matcher
from ..._models import BaseModel

__all__ = ["AccountRule", "Zone"]


class Zone(BaseModel):
    """Zone information for the routing rule."""

    name: Optional[str] = None
    """Zone name."""

    tag: Optional[str] = None
    """Zone tag."""


class AccountRule(BaseModel):
    id: Optional[str] = None
    """Routing rule identifier."""

    actions: Optional[List[Action]] = None
    """List actions patterns."""

    enabled: Optional[Literal[True, False]] = None
    """Routing rule status."""

    matchers: Optional[List[Matcher]] = None
    """Matching patterns to forward to your actions."""

    name: Optional[str] = None
    """Routing rule name."""

    priority: Optional[float] = None
    """Priority of the routing rule."""

    source: Optional[Literal["api", "wrangler"]] = None
    """Who manages the rule.

    `api` covers dashboard, generic API, and Terraform; `wrangler` means the rule is
    managed by a Worker's wrangler.jsonc. Defaults to `api` when omitted on write.
    """

    tag: Optional[str] = None
    """Routing rule tag. (Deprecated, replaced by routing rule identifier)"""

    zone: Optional[Zone] = None
    """Zone information for the routing rule."""
