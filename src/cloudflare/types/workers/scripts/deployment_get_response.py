# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DeploymentGetResponse", "Deployment", "DeploymentVersion", "DeploymentAnnotations"]


class DeploymentVersion(BaseModel):
    percentage: float

    version_id: str


class DeploymentAnnotations(BaseModel):
    workers_message: Optional[str] = FieldInfo(alias="workers/message", default=None)
    """Human-readable message about the deployment. Truncated to 100 bytes."""


class Deployment(BaseModel):
    id: str

    created_on: datetime

    source: str

    strategy: Literal["percentage"]

    versions: List[DeploymentVersion]

    annotations: Optional[DeploymentAnnotations] = None

    author_email: Optional[str] = None


class DeploymentGetResponse(BaseModel):
    deployments: List[Deployment]
