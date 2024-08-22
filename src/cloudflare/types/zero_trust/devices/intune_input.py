# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["IntuneInput"]

class IntuneInput(BaseModel):
    compliance_status: Literal["compliant", "noncompliant", "unknown", "notapplicable", "ingraceperiod", "error"]
    """Compliance Status"""

    connection_id: str
    """Posture Integration ID."""