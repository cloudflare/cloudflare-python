# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ConfigurationDeleteResponse"]


class ConfigurationDeleteResponse(BaseModel):
    id: Optional[str] = None
    """UUID."""
