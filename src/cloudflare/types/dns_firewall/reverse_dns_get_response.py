# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from ..._models import BaseModel

__all__ = ["ReverseDNSGetResponse"]


class ReverseDNSGetResponse(BaseModel):
    ptr: Dict[str, str]
    """Map of cluster IP addresses to PTR record contents"""
