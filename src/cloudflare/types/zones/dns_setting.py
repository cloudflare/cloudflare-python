# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .nameserver import Nameserver

__all__ = ["DNSSetting"]


class DNSSetting(BaseModel):
    nameservers: Optional[Nameserver] = None
    """
    Settings determining the nameservers through which the zone should be available.
    """
