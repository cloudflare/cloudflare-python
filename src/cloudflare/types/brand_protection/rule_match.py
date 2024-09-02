# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["RuleMatch"]


class RuleMatch(BaseModel):
    banning: Optional[bool] = None
    """For internal use."""

    blocking: Optional[bool] = None
    """For internal use."""

    description: Optional[str] = None
    """Description of the signature that matched."""

    name: Optional[str] = None
    """Name of the signature that matched."""
