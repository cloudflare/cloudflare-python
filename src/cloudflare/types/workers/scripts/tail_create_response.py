# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["TailCreateResponse"]

class TailCreateResponse(BaseModel):
    id: Optional[str] = None

    expires_at: Optional[str] = None

    url: Optional[str] = None