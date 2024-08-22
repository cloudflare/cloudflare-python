# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing_extensions import Literal

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Action"]

class Action(BaseModel):
    type: Literal["drop", "forward", "worker"]
    """Type of supported action."""

    value: List[str]