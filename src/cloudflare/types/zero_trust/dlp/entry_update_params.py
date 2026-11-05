# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ...._types import SequenceNotStr
from .profiles.pattern_param import PatternParam

__all__ = ["EntryUpdateParams", "Variant0", "Variant1", "Variant2"]


class Variant0(TypedDict, total=False):
    account_id: Required[str]

    name: Required[str]

    pattern: Required[PatternParam]

    type: Required[Literal["custom"]]

    description: Optional[str]

    enabled: bool

    validator_ids: SequenceNotStr[str]
    """Validators this entry should reference, by id, at most 10.

    Replaces the current set.

    Optional, unlike the rest of this body: omitting it leaves the current
    attachments alone, so a client that predates validators cannot detach them by
    accident. Send `[]` to detach.
    """


class Variant1(TypedDict, total=False):
    account_id: Required[str]

    type: Required[Literal["predefined"]]

    enabled: bool


class Variant2(TypedDict, total=False):
    account_id: Required[str]

    type: Required[Literal["integration"]]

    enabled: bool


EntryUpdateParams: TypeAlias = Union[Variant0, Variant1, Variant2]
