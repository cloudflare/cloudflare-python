# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["DeploymentsByScriptDetailResponse"]


class DeploymentsByScriptDetailResponse(BaseModel):
    id: Optional[str] = None

    metadata: Optional[object] = None

    number: Optional[float] = None

    resources: Optional[object] = None
