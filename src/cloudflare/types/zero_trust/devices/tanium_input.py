# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["TaniumInput"]


class TaniumInput(BaseModel):
    connection_id: str
    """Posture Integration ID."""

    eid_last_seen: Optional[str] = None
    """For more details on eid last seen, refer to the Tanium documentation."""

    operator: Optional[Literal["<", "<=", ">", ">=", "=="]] = None
    """Operator to evaluate risk_level or eid_last_seen."""

    risk_level: Optional[Literal["low", "medium", "high", "critical"]] = None
    """For more details on risk level, refer to the Tanium documentation."""

    score_operator: Optional[Literal["<", "<=", ">", ">=", "=="]] = FieldInfo(alias="scoreOperator", default=None)
    """Score Operator"""

    total_score: Optional[float] = None
    """For more details on total score, refer to the Tanium documentation."""
