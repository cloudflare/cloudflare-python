# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["Pagerduty"]


class Pagerduty(BaseModel):
    id: Optional[str] = None
    """UUID"""

    name: Optional[str] = None
    """The name of the pagerduty service."""
