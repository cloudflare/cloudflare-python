# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["AuditSSHSettingGetResponse"]


class AuditSSHSettingGetResponse(BaseModel):
    created_at: Optional[datetime] = None

    public_key: Optional[str] = None
    """SSH encryption public key"""

    seed_id: Optional[str] = None
    """Seed ID"""

    updated_at: Optional[datetime] = None
