# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["IP", "BelongsToRef"]

class BelongsToRef(BaseModel):
    id: Optional[str] = None

    country: Optional[str] = None

    description: Optional[str] = None

    type: Optional[Literal["hosting_provider", "isp", "organization"]] = None
    """Infrastructure type of this ASN."""

    value: Optional[str] = None

class IP(BaseModel):
    belongs_to_ref: Optional[BelongsToRef] = None
    """
    Specifies a reference to the autonomous systems (AS) that the IP address belongs
    to.
    """

    ip: Optional[str] = None

    risk_types: Optional[List[object]] = None