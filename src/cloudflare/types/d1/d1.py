# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["D1"]

class D1(BaseModel):
    created_at: Optional[datetime] = None
    """Specifies the timestamp the resource was created as an ISO8601 string."""

    file_size: Optional[float] = None
    """The D1 database's size, in bytes."""

    name: Optional[str] = None

    num_tables: Optional[float] = None

    uuid: Optional[str] = None

    version: Optional[str] = None