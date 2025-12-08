# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "RuleBulkEditParams",
    "Body",
    "BodyPosition",
    "BodyPositionAPIShieldIndex",
    "BodyPositionAPIShieldBefore",
    "BodyPositionAPIShieldAfter",
    "BodySelector",
    "BodySelectorExclude",
    "BodySelectorInclude",
]


class RuleBulkEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    body: Required[Iterable[Body]]


class BodyPositionAPIShieldIndex(TypedDict, total=False):
    index: Required[int]
    """Move rule to this position"""


class BodyPositionAPIShieldBefore(TypedDict, total=False):
    """Move rule to after rule with ID."""

    before: str
    """Move rule to before rule with this ID."""


class BodyPositionAPIShieldAfter(TypedDict, total=False):
    """Move rule to before rule with ID."""

    after: str
    """Move rule to after rule with this ID."""


BodyPosition: TypeAlias = Union[BodyPositionAPIShieldIndex, BodyPositionAPIShieldBefore, BodyPositionAPIShieldAfter]


class BodySelectorExclude(TypedDict, total=False):
    operation_ids: SequenceNotStr[str]
    """Excluded operation IDs."""


class BodySelectorInclude(TypedDict, total=False):
    host: SequenceNotStr[str]
    """Included hostnames."""


class BodySelector(TypedDict, total=False):
    """Select operations covered by this rule.

    For details on selectors, see the [Cloudflare Docs](https://developers.cloudflare.com/api-shield/security/jwt-validation/).
    """

    exclude: Optional[Iterable[BodySelectorExclude]]
    """Ignore operations that were otherwise included by `include`."""

    include: Optional[Iterable[BodySelectorInclude]]
    """Select all matching operations."""


class Body(TypedDict, total=False):
    id: Required[str]
    """Rule ID this patch applies to"""

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

    position: BodyPosition
    """Update rule order among zone rules."""

    selector: BodySelector
    """Select operations covered by this rule.

    For details on selectors, see the
    [Cloudflare Docs](https://developers.cloudflare.com/api-shield/security/jwt-validation/).
    """

    title: str
    """A human-readable name for the rule."""
