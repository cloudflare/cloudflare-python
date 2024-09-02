# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, TypeAlias

from typing import Iterable, Union

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ....._types import FileTypes
from ....._utils import PropertyInfo

__all__ = ["VersionCreateParams", "Body", "BodyExistingColumn", "BodyNewColumn"]


class VersionCreateParams(TypedDict, total=False):
    account_id: Required[str]

    dataset_id: Required[str]

    body: Required[Iterable[Body]]


class BodyExistingColumn(TypedDict, total=False):
    entry_id: Required[str]


class BodyNewColumn(TypedDict, total=False):
    entry_name: Required[str]


Body: TypeAlias = Union[BodyExistingColumn, BodyNewColumn]
