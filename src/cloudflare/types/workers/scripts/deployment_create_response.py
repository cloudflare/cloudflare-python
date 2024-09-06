# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing_extensions import Literal

from typing import List, Optional

from .deployment import Deployment

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["DeploymentCreateResponse", "Version"]


class Version(BaseModel):
    percentage: float

    version_id: str


class DeploymentCreateResponse(BaseModel):
    strategy: Literal["percentage"]

    versions: List[Version]

    id: Optional[str] = None

    annotations: Optional[Deployment] = None

    author_email: Optional[str] = None

    created_on: Optional[str] = None

    source: Optional[str] = None
