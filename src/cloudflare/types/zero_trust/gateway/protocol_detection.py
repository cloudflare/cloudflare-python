# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ProtocolDetection"]


class ProtocolDetection(BaseModel):
    enabled: Optional[bool] = None
    """Enable detecting protocol on initial bytes of client traffic."""
