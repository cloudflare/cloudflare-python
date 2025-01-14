# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["ReverseDNSEditResponse"]


class ReverseDNSEditResponse(BaseModel):
    ptr: Optional[Dict[str, str]] = None
    """Map of cluster IP addresses to PTR record contents"""
