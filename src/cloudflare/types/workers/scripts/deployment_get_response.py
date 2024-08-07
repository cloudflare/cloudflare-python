# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from . import deployment
from ...._models import BaseModel

__all__ = ["DeploymentGetResponse", "Deployment"]


class Deployment(BaseModel):
    strategy: str

    id: Optional[str] = None

    annotations: Optional[deployment.Deployment] = None

    author_email: Optional[str] = None

    created_on: Optional[str] = None

    source: Optional[str] = None


class DeploymentGetResponse(BaseModel):
    deployments: Optional[List[Deployment]] = None
