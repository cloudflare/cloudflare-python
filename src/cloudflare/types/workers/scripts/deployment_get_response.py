# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .unnamed_schema_ref_fda1c6f6758e763ae3b2964521f2fdd8 import UnnamedSchemaRefFda1c6f6758e763ae3b2964521f2fdd8

__all__ = ["DeploymentGetResponse", "Deployment"]


class Deployment(BaseModel):
    id: Optional[str] = None

    annotations: Optional[UnnamedSchemaRefFda1c6f6758e763ae3b2964521f2fdd8] = None

    author_email: Optional[str] = None

    created_on: Optional[str] = None

    source: Optional[str] = None

    strategy: Optional[str] = None


class DeploymentGetResponse(BaseModel):
    deployments: Optional[List[Deployment]] = None
