# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["KolideInput"]


class KolideInput(BaseModel):
    connection_id: str
    """Posture Integration ID."""

    auth_state: Optional[List[Literal["Good", "Notified", "Will Block", "Blocked"]]] = None
    """The set of Kolide device authentication states that pass the posture check.

    Device must match one of the specified states.
    """

    count_operator: Optional[Literal["<", "<=", ">", ">=", "=="]] = FieldInfo(alias="countOperator", default=None)
    """Count Operator."""

    issue_count: Optional[str] = None
    """The Number of Issues."""
