# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["SnapshotListParams"]


class SnapshotListParams(TypedDict, total=False):
    account_id: Required[float]

    from_: Required[Annotated[float, PropertyInfo(alias="from")]]

    to: Required[float]

    cursor: str

    limit: float
