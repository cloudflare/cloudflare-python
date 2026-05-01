# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["DeploymentGroupDeleteResponse"]


class DeploymentGroupDeleteResponse(BaseModel):
    id: Optional[str] = None
    """The ID of a deleted deployment group."""
