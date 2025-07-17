# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DeploymentCreateResponse", "Version", "Annotations"]


class Version(BaseModel):
    percentage: float

    version_id: str


class Annotations(BaseModel):
    workers_message: Optional[str] = FieldInfo(alias="workers/message", default=None)
    """Human-readable message about the deployment. Truncated to 100 bytes."""


class DeploymentCreateResponse(BaseModel):
    id: str

    created_on: datetime

    source: str

    strategy: Literal["percentage"]

    versions: List[Version]

    annotations: Optional[Annotations] = None

    author_email: Optional[str] = None
