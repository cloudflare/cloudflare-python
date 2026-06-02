# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo

__all__ = ["StatusEditParams", "Variant0", "Variant1", "Variant2", "Variant3", "Variant3From"]


class Variant0(TypedDict, total=False):
    account_id: Required[str]

    workflow_name: Required[str]

    status: Required[Literal["pause"]]


class Variant1(TypedDict, total=False):
    account_id: Required[str]

    workflow_name: Required[str]

    status: Required[Literal["resume"]]


class Variant2(TypedDict, total=False):
    account_id: Required[str]

    workflow_name: Required[str]

    status: Required[Literal["terminate"]]

    rollback: bool
    """Run rollback before terminating."""


class Variant3(TypedDict, total=False):
    account_id: Required[str]

    workflow_name: Required[str]

    status: Required[Literal["restart"]]

    from_: Annotated[Variant3From, PropertyInfo(alias="from")]
    """Step to restart from."""


class Variant3From(TypedDict, total=False):
    """Step to restart from."""

    name: Required[str]

    count: int

    type: Literal["do", "sleep", "waitForEvent"]


StatusEditParams: TypeAlias = Union[Variant0, Variant1, Variant2, Variant3]
