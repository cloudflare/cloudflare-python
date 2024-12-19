# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel
from .gateway_configuration_settings import GatewayConfigurationSettings

__all__ = ["ConfigurationUpdateResponse"]


class ConfigurationUpdateResponse(BaseModel):
    created_at: Optional[datetime] = None

    settings: Optional[GatewayConfigurationSettings] = None
    """Account settings"""

    updated_at: Optional[datetime] = None
