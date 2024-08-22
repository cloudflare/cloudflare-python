# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing_extensions import Literal

from typing import List, Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Ciphers"]

class Ciphers(BaseModel):
    id: Literal["ciphers"]
    """ID of the zone setting."""

    value: List[str]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""