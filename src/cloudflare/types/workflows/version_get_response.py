# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["VersionGetResponse", "Limits"]


class Limits(BaseModel):
    steps: Optional[int] = None


class VersionGetResponse(BaseModel):
    id: str

    class_name: str

    created_on: datetime

    has_dag: bool

    modified_on: datetime

    workflow_id: str

    limits: Optional[Limits] = None
