# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["KolideInput"]


class KolideInput(BaseModel):
    connection_id: str
    """Posture Integration ID."""

    count_operator: Literal["<", "<=", ">", ">=", "=="] = FieldInfo(alias="countOperator")
    """Count Operator"""

    issue_count: str
    """The Number of Issues."""
