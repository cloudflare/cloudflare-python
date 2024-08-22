# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["RuleCreateParams"]


class RuleCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    host: str

    inclusive: bool
    """Whether the rule includes or excludes traffic from being measured."""

    is_paused: bool
    """Whether the rule is paused or not."""

    paths: List[str]
