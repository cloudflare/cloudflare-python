# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["KolideInputParam"]


class KolideInputParam(TypedDict, total=False):
    connection_id: Required[str]
    """Posture Integration ID."""

    count_operator: Required[Annotated[Literal["<", "<=", ">", ">=", "=="], PropertyInfo(alias="countOperator")]]
    """Count Operator"""

    issue_count: Required[str]
    """The Number of Issues."""
