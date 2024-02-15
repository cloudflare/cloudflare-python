# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["DeploymentsByScriptListResponse"]


class DeploymentsByScriptListResponse(BaseModel):
    items: Optional[List[object]] = None

    latest: Optional[object] = None
