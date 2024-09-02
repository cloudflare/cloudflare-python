# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["TokenCreateResponse"]


class TokenCreateResponse(BaseModel):
    token: Optional[str] = None
    """The signed token used with the signed URLs feature."""
