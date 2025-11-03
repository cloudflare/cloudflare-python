# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TokenValidationRule", "Selector", "SelectorExclude", "SelectorInclude"]


class SelectorExclude(BaseModel):
    operation_ids: Optional[List[str]] = None
    """Excluded operation IDs."""


class SelectorInclude(BaseModel):
    host: Optional[List[str]] = None
    """Included hostnames."""


class Selector(BaseModel):
    exclude: Optional[List[SelectorExclude]] = None
    """Ignore operations that were otherwise included by `include`."""

    include: Optional[List[SelectorInclude]] = None
    """Select all matching operations."""


class TokenValidationRule(BaseModel):
    action: Literal["log", "block"]
    """
    Action to take on requests that match operations included in `selector` and fail
    `expression`.
    """

    description: str
    """A human-readable description that gives more details than `title`."""

    enabled: bool
    """Toggle rule on or off."""

    expression: str
    """Rule expression.

    Requests that fail to match this expression will be subject to `action`.

    For details on expressions, see the
    [Cloudflare Docs](https://developers.cloudflare.com/api-shield/security/jwt-validation/).
    """

    selector: Selector
    """Select operations covered by this rule.

    For details on selectors, see the
    [Cloudflare Docs](https://developers.cloudflare.com/api-shield/security/jwt-validation/).
    """

    title: str
    """A human-readable name for the rule."""

    id: Optional[str] = None
    """UUID."""

    created_at: Optional[datetime] = None

    last_updated: Optional[datetime] = None
