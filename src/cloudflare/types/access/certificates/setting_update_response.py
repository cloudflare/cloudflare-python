# File generated from our OpenAPI spec by Stainless.

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["SettingUpdateResponse", "SettingUpdateResponseItem"]


class SettingUpdateResponseItem(BaseModel):
    china_network: bool
    """Request client certificates for this hostname in China.

    Can only be set to true if this zone is china network enabled.
    """

    client_certificate_forwarding: bool
    """
    Client Certificate Forwarding is a feature that takes the client cert provided
    by the eyeball to the edge, and forwards it to the origin as a HTTP header to
    allow logging on the origin.
    """

    hostname: str
    """The hostname that these settings apply to."""


SettingUpdateResponse = List[SettingUpdateResponseItem]
