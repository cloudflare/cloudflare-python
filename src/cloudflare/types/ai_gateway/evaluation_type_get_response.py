# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["EvaluationTypeGetResponse", "EvaluationTypeGetResponseItem"]


class EvaluationTypeGetResponseItem(BaseModel):
    id: str

    created_at: datetime

    description: str

    enable: bool

    mandatory: bool

    modified_at: datetime

    name: str

    type: str


EvaluationTypeGetResponse: TypeAlias = List[EvaluationTypeGetResponseItem]
