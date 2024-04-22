# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...shared import UnnamedSchemaRef125
from ...._models import BaseModel

__all__ = ["ConfigurationUpdateResponse"]


class ConfigurationUpdateResponse(BaseModel):
    created_at: Optional[datetime] = None

    settings: Optional[UnnamedSchemaRef125] = None
    """account settings."""

    updated_at: Optional[datetime] = None
