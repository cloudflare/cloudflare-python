# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["RuleFirewallRulesListFirewallRulesParams"]


class RuleFirewallRulesListFirewallRulesParams(TypedDict, total=False):
    action: str
    """The action to search for. Must be an exact match."""

    description: str
    """A case-insensitive string to find in the description."""

    page: float
    """Page number of paginated results."""

    paused: bool
    """When true, indicates that the firewall rule is currently paused."""

    per_page: float
    """Number of firewall rules per page."""
