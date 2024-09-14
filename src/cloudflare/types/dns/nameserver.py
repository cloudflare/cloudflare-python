# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Nameserver"]


class Nameserver(BaseModel):
    type: Literal["cloudflare.standard", "cloudflare.standard.random", "custom.account", "custom.tenant", "custom.zone"]
    """Nameserver type"""
