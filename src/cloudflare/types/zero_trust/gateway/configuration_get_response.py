# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel
from .gateway_configuration_settings import GatewayConfigurationSettings

__all__ = ["ConfigurationGetResponse"]


class ConfigurationGetResponse(BaseModel):
    """Specify account settings."""

    created_at: Optional[datetime] = None

    settings: Optional[GatewayConfigurationSettings] = None
    """Specify account settings."""

    updated_at: Optional[datetime] = None
