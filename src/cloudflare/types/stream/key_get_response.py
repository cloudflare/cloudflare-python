# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from datetime import datetime

from typing_extensions import TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["KeyGetResponse", "KeyGetResponseItem"]


class KeyGetResponseItem(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    created: Optional[datetime] = None
    """The date and time a signing key was created."""


KeyGetResponse: TypeAlias = List[KeyGetResponseItem]
