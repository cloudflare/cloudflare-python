# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TaniumInputParam"]


class TaniumInputParam(TypedDict, total=False):
    connection_id: Required[str]
    """Posture Integration ID."""

    eid_last_seen: str
    """For more details on eid last seen, refer to the Tanium documentation."""

    operator: Literal["<", "<=", ">", ">=", "=="]
    """Operator to evaluate risk_level or eid_last_seen."""

    risk_level: Literal["low", "medium", "high", "critical"]
    """For more details on risk level, refer to the Tanium documentation."""

    score_operator: Annotated[Literal["<", "<=", ">", ">=", "=="], PropertyInfo(alias="scoreOperator")]
    """Score Operator"""

    total_score: float
    """For more details on total score, refer to the Tanium documentation."""
