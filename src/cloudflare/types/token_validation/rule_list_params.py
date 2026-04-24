# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["RuleListParams"]


class RuleListParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    id: str
    """Select rules with these IDs."""

    action: Literal["log", "block"]
    """
    Action to take on requests that match operations included in `selector` and fail
    `expression`.
    """

    enabled: bool
    """Toggle rule on or off."""

    host: str
    """Select rules with this host in `include`."""

    hostname: str
    """Select rules with this host in `include`."""

    page: int
    """Page number of paginated results."""

    per_page: int
    """Maximum number of results per page."""

    rule_id: str
    """Select rules with these IDs."""

    token_configuration: SequenceNotStr[str]
    """Select rules using any of these token configurations."""
