# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ProtocolDetection"]


class ProtocolDetection(BaseModel):
    """Specify whether to detect protocols from the initial bytes of client traffic."""

    enabled: Optional[bool] = None
    """Specify whether to detect protocols from the initial bytes of client traffic."""
