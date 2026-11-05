# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WorkflowUpdateResponse"]


class WorkflowUpdateResponse(BaseModel):
    id: str

    class_name: str

    created_on: datetime

    is_deleted: float

    modified_on: datetime

    name: str

    script_name: str

    terminator_running: float

    triggered_on: Optional[datetime] = None

    version_id: str

    jurisdiction: Optional[Literal["eu", "fedramp", "us"]] = None
    """Jurisdiction where instances of this workflow run and store data.

    Set when the workflow is created and cannot be changed.
    """
