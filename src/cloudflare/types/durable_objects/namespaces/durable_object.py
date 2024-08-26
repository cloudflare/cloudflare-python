# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["DurableObject"]

class DurableObject(BaseModel):
    id: Optional[str] = None
    """ID of the Durable Object."""

    has_stored_data: Optional[bool] = FieldInfo(alias = "hasStoredData", default = None)
    """Whether the Durable Object has stored data."""