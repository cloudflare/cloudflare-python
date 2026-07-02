# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .action_param import ActionParam
from .matcher_param import MatcherParam

__all__ = ["RuleCreateParams"]


class RuleCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    actions: Required[Iterable[ActionParam]]
    """List actions patterns."""

    matchers: Required[Iterable[MatcherParam]]
    """Matching patterns to forward to your actions."""

    enabled: Literal[True, False]
    """Routing rule status."""

    name: str
    """Routing rule name."""

    owner_worker_tag: str
    """Public tag (script_tag) of the Worker that owns this rule.

    Required when `source` is `wrangler`.
    """

    priority: float
    """Priority of the routing rule."""

    source: Literal["api", "wrangler"]
    """Who manages the rule.

    `api` covers dashboard, generic API, and Terraform; `wrangler` means the rule is
    managed by a Worker's wrangler.jsonc. Defaults to `api` when omitted on write.
    """
