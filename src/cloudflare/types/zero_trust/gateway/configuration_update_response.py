# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from datetime import datetime

from .gateway_configuration_settings import GatewayConfigurationSettings

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ConfigurationUpdateResponse"]


class ConfigurationUpdateResponse(BaseModel):
    created_at: Optional[datetime] = None

    settings: Optional[GatewayConfigurationSettings] = None
    """account settings."""

    updated_at: Optional[datetime] = None
