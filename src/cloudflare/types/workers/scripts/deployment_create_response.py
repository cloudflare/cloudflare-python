# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from .deployment import Deployment

__all__ = ["DeploymentCreateResponse"]


class DeploymentCreateResponse(BaseModel):
    strategy: str

    id: Optional[str] = None

    annotations: Optional[Deployment] = None

    author_email: Optional[str] = None

    created_on: Optional[str] = None

    source: Optional[str] = None
