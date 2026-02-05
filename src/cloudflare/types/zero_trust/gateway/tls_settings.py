# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["TLSSettings"]


class TLSSettings(BaseModel):
    """Specify whether to inspect encrypted HTTP traffic."""

    enabled: Optional[bool] = None
    """Specify whether to inspect encrypted HTTP traffic."""
