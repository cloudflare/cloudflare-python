# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

from ...radar_email_series import RadarEmailSeries

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["TimeseriesGroupSPFResponse"]

class TimeseriesGroupSPFResponse(BaseModel):
    meta: object

    serie_0: RadarEmailSeries