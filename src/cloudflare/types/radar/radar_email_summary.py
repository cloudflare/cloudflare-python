# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RadarEmailSummary"]


class RadarEmailSummary(BaseModel):
    fail: str = FieldInfo(alias="FAIL")

    none: str = FieldInfo(alias="NONE")

    pass_: str = FieldInfo(alias="PASS")
