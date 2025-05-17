# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["TelemetryValuesResponse"]


class TelemetryValuesResponse(BaseModel):
    dataset: str

    key: str

    type: Literal["string", "boolean", "number"]

    value: Union[str, float, bool]
