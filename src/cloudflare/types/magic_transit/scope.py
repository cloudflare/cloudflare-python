# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Scope"]


class Scope(BaseModel):
    colo_names: Optional[List[str]] = None
    """List of colo names for the ECMP scope."""

    colo_regions: Optional[List[str]] = None
    """List of colo regions for the ECMP scope."""
