# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "RuleEditParams",
    "Position",
    "PositionAPIShieldIndex",
    "PositionAPIShieldBefore",
    "PositionAPIShieldAfter",
    "Selector",
    "SelectorExclude",
    "SelectorInclude",
]


class RuleEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

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

    position: Position
    """Update rule order among zone rules."""

    selector: Selector
    """Select operations covered by this rule.

    For details on selectors, see the
    [Cloudflare Docs](https://developers.cloudflare.com/api-shield/security/jwt-validation/).
    """

    title: str
    """A human-readable name for the rule."""


class PositionAPIShieldIndex(TypedDict, total=False):
    index: Required[int]
    """Move rule to this position"""


class PositionAPIShieldBefore(TypedDict, total=False):
    before: str
    """Move rule to before rule with this ID."""


class PositionAPIShieldAfter(TypedDict, total=False):
    after: str
    """Move rule to after rule with this ID."""


Position: TypeAlias = Union[PositionAPIShieldIndex, PositionAPIShieldBefore, PositionAPIShieldAfter]


class SelectorExclude(TypedDict, total=False):
    operation_ids: SequenceNotStr[str]
    """Excluded operation IDs."""


class SelectorInclude(TypedDict, total=False):
    host: SequenceNotStr[str]
    """Included hostnames."""


class Selector(TypedDict, total=False):
    exclude: Optional[Iterable[SelectorExclude]]
    """Ignore operations that were otherwise included by `include`."""

    include: Optional[Iterable[SelectorInclude]]
    """Select all matching operations."""
