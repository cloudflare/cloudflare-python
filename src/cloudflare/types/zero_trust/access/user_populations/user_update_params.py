# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["UserUpdateParams", "Operation"]


class UserUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    user_population_id: Required[str]
    """UUID."""

    operations: Required[Annotated[Iterable[Operation], PropertyInfo(alias="Operations")]]

    schemas: SequenceNotStr[str]


class Operation(TypedDict, total=False):
    op: Required[Literal["add", "remove", "replace"]]

    path: str

    value: Union[Optional[str], float, bool, Iterable[object], Dict[str, object]]
