# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing_extensions import Literal

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["CatchAllAction"]

class CatchAllAction(BaseModel):
    type: Literal["drop", "forward", "worker"]
    """Type of action for catch-all rule."""

    value: Optional[List[str]] = None