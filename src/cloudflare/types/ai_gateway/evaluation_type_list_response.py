# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["EvaluationTypeListResponse"]


class EvaluationTypeListResponse(BaseModel):
    id: str

    created_at: datetime

    description: str

    enable: bool

    mandatory: bool

    modified_at: datetime

    name: str

    type: str
