# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["RuleBulkCreateParams", "Rule"]


class RuleBulkCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    delete_rules: SequenceNotStr[str]
    """A list of rule identifiers to delete."""

    rules: Iterable[Rule]
    """A list of rules to create or update."""


class Rule(TypedDict, total=False):
    id: str
    """The Web Analytics rule identifier."""

    host: str

    inclusive: bool

    is_paused: bool

    paths: SequenceNotStr[str]
