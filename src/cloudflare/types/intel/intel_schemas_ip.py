# File generated from our OpenAPI spec by Stainless.

from typing import Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["IntelSchemasIP", "BelongsToRef"]


class BelongsToRef(BaseModel):
    id: Optional[object] = None

    country: Optional[str] = None

    description: Optional[str] = None

    type: Optional[Literal["hosting_provider", "isp", "organization"]] = None
    """Infrastructure type of this ASN."""

    value: Optional[str] = None


class IntelSchemasIP(BaseModel):
    belongs_to_ref: Optional[BelongsToRef] = None
    """
    Specifies a reference to the autonomous systems (AS) that the IP address belongs
    to.
    """

    ip: Union[str, str, None] = None

    risk_types: Optional[object] = None
