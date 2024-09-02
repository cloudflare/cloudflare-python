# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing_extensions import Literal

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["DomainJoinedInput"]


class DomainJoinedInput(BaseModel):
    operating_system: Literal["windows"]
    """Operating System"""

    domain: Optional[str] = None
    """Domain"""
