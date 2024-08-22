# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from datetime import datetime

from .setting_value import SettingValue

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["TLSDeleteResponse"]

class TLSDeleteResponse(BaseModel):
    created_at: Optional[datetime] = None
    """This is the time the tls setting was originally created for this hostname."""

    hostname: Optional[str] = None
    """The hostname for which the tls settings are set."""

    status: Optional[str] = None
    """Deployment status for the given tls setting."""

    updated_at: Optional[datetime] = None
    """This is the time the tls setting was updated."""

    value: Optional[SettingValue] = None
    """The tls setting value."""