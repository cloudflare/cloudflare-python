# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["RuleCreateParams", "Selector", "SelectorExclude", "SelectorInclude"]


class RuleCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    action: Required[Literal["log", "block"]]
    """
    Action to take on requests that match operations included in `selector` and fail
    `expression`.
    """

    description: Required[str]
    """A human-readable description that gives more details than `title`."""

    enabled: Required[bool]
    """Toggle rule on or off."""

    expression: Required[str]
    """Rule expression.

    Requests that fail to match this expression will be subject to `action`.

    For details on expressions, see the
    [Cloudflare Docs](https://developers.cloudflare.com/api-shield/security/jwt-validation/).
    """

    selector: Required[Selector]
    """Select operations covered by this rule.

    For details on selectors, see the
    [Cloudflare Docs](https://developers.cloudflare.com/api-shield/security/jwt-validation/).
    """

    title: Required[str]
    """A human-readable name for the rule."""


class SelectorExclude(TypedDict, total=False):
    operation_ids: SequenceNotStr[str]
    """Excluded operation IDs."""


class SelectorInclude(TypedDict, total=False):
    host: SequenceNotStr[str]
    """Included hostnames."""


class Selector(TypedDict, total=False):
    """Select operations covered by this rule.

    For details on selectors, see the [Cloudflare Docs](https://developers.cloudflare.com/api-shield/security/jwt-validation/).
    """

    exclude: Optional[Iterable[SelectorExclude]]
    """Ignore operations that were otherwise included by `include`."""

    include: Optional[Iterable[SelectorInclude]]
    """Select all matching operations."""
