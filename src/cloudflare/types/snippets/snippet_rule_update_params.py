# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import Iterable

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["SnippetRuleUpdateParams", "Rule"]


class SnippetRuleUpdateParams(TypedDict, total=False):
    rules: Iterable[Rule]
    """List of snippet rules"""


class Rule(TypedDict, total=False):
    description: str

    enabled: bool

    expression: str

    snippet_name: str
    """Snippet identifying name"""
