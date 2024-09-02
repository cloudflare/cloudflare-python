# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["KolideInput"]


class KolideInput(BaseModel):
    connection_id: str
    """Posture Integration ID."""

    count_operator: Literal["<", "<=", ">", ">=", "=="] = FieldInfo(alias="countOperator")
    """Count Operator"""

    issue_count: str
    """The Number of Issues."""
