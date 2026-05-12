# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["AISecurityUpdateResponse"]


class AISecurityUpdateResponse(BaseModel):
    """AI Security for Apps enablement status for a zone."""

    enabled: Optional[bool] = None
    """Whether AI Security for Apps is enabled on the zone."""
