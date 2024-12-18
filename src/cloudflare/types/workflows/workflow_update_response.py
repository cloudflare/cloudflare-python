# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["WorkflowUpdateResponse"]


class WorkflowUpdateResponse(BaseModel):
    id: str

    class_name: str

    created_on: datetime

    modified_on: datetime

    name: str

    script_name: str

    triggered_on: Optional[datetime] = None

    version_id: str
