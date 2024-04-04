# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DeploymentCreateResponse", "Annotations"]


class Annotations(BaseModel):
    workers_message: Optional[str] = FieldInfo(alias="workers/message", default=None)
    """Human-readable message about the deployment."""


class DeploymentCreateResponse(BaseModel):
    id: Optional[str] = None

    annotations: Optional[Annotations] = None

    author_email: Optional[str] = None

    created_on: Optional[str] = None

    source: Optional[str] = None

    strategy: Optional[str] = None
