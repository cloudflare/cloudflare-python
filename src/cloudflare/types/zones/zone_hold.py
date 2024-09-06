# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ZoneHold"]


class ZoneHold(BaseModel):
    hold: Optional[bool] = None

    hold_after: Optional[str] = None

    include_subdomains: Optional[str] = None
