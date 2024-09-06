# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing_extensions import Literal

from typing import List, Optional

from . import deployment

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["DeploymentGetResponse", "Deployment", "DeploymentVersion"]


class DeploymentVersion(BaseModel):
    percentage: float

    version_id: str


class Deployment(BaseModel):
    strategy: Literal["percentage"]

    versions: List[DeploymentVersion]

    id: Optional[str] = None

    annotations: Optional[deployment.Deployment] = None

    author_email: Optional[str] = None

    created_on: Optional[str] = None

    source: Optional[str] = None


class DeploymentGetResponse(BaseModel):
    deployments: Optional[List[Deployment]] = None
