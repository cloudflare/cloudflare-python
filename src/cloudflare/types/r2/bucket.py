# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Bucket"]

class Bucket(BaseModel):
    creation_date: Optional[str] = None
    """Creation timestamp"""

    location: Optional[Literal["apac", "eeur", "enam", "weur", "wnam"]] = None
    """Location of the bucket"""

    name: Optional[str] = None
    """Name of the bucket"""

    storage_class: Optional[Literal["Standard", "InfrequentAccess"]] = None
    """Storage class for newly uploaded objects, unless specified otherwise."""