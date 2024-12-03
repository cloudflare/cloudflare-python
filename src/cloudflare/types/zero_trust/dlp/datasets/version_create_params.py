# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["VersionCreateParams", "Body", "BodyExistingColumn", "BodyNewColumn"]


class VersionCreateParams(TypedDict, total=False):
    account_id: Required[str]

    dataset_id: Required[str]

    body: Required[Iterable[Body]]


class BodyExistingColumn(TypedDict, total=False):
    entry_id: Required[str]

    header_name: str

    num_cells: int


class BodyNewColumn(TypedDict, total=False):
    entry_name: Required[str]

    header_name: str

    num_cells: int


Body: TypeAlias = Union[BodyExistingColumn, BodyNewColumn]
