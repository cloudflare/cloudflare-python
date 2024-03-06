# File generated from our OpenAPI spec by Stainless.

from typing import List, Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["IPGetResponse", "IPGetResponseItem", "IPGetResponseItemBelongsToRef"]


class IPGetResponseItemBelongsToRef(BaseModel):
    id: Optional[object] = None

    country: Optional[str] = None

    description: Optional[str] = None

    type: Optional[Literal["hosting_provider", "isp", "organization"]] = None
    """Infrastructure type of this ASN."""

    value: Optional[str] = None


class IPGetResponseItem(BaseModel):
    belongs_to_ref: Optional[IPGetResponseItemBelongsToRef] = None
    """
    Specifies a reference to the autonomous systems (AS) that the IP address belongs
    to.
    """

    ip: Union[str, str, None] = None

    risk_types: Optional[object] = None


IPGetResponse = List[IPGetResponseItem]
