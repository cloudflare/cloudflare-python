# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["VersionListResponse"]

class VersionListResponse(BaseModel):
    id: Optional[str] = None

    metadata: Optional[object] = None

    number: Optional[float] = None