# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RadarEmailSummary"]


class RadarEmailSummary(BaseModel):
    fail: str = FieldInfo(alias="FAIL")
    """A numeric string."""

    none: str = FieldInfo(alias="NONE")
    """A numeric string."""

    pass_: str = FieldInfo(alias="PASS")
    """A numeric string."""
