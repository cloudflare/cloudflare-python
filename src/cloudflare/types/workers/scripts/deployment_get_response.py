# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DeploymentGetResponse", "Deployment", "DeploymentAnnotations"]


class DeploymentAnnotations(BaseModel):
    workers_message: Optional[str] = FieldInfo(alias="workers/message", default=None)
    """Human-readable message about the deployment."""


class Deployment(BaseModel):
    id: Optional[str] = None

    annotations: Optional[DeploymentAnnotations] = None

    author_email: Optional[str] = None

    created_on: Optional[str] = None

    source: Optional[str] = None

    strategy: Optional[str] = None


class DeploymentGetResponse(BaseModel):
    deployments: Optional[List[Deployment]] = None
