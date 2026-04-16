# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["KolideInputParam"]


class KolideInputParam(TypedDict, total=False):
    connection_id: Required[str]
    """Posture Integration ID."""

    auth_state: List[Literal["Good", "Notified", "Will Block", "Blocked"]]
    """The set of Kolide device authentication states that pass the posture check.

    Device must match one of the specified states.
    """

    count_operator: Annotated[Literal["<", "<=", ">", ">=", "=="], PropertyInfo(alias="countOperator")]
    """Count Operator."""

    issue_count: str
    """The Number of Issues."""
