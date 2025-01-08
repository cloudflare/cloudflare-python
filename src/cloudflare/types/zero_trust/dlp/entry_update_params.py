# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .profiles.pattern_param import PatternParam

__all__ = ["EntryUpdateParams", "Variant0", "Variant1", "Variant2"]


class Variant0(TypedDict, total=False):
    account_id: Required[str]

    name: Required[str]

    pattern: Required[PatternParam]

    type: Required[Literal["custom"]]

    enabled: bool


class Variant1(TypedDict, total=False):
    account_id: Required[str]

    type: Required[Literal["predefined"]]

    enabled: bool


class Variant2(TypedDict, total=False):
    account_id: Required[str]

    type: Required[Literal["integration"]]

    enabled: bool


EntryUpdateParams: TypeAlias = Union[Variant0, Variant1, Variant2]
