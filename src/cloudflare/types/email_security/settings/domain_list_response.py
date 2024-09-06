# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import List, Optional

from typing_extensions import Literal

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["DomainListResponse"]


class DomainListResponse(BaseModel):
    id: int
    """Unique domain identifier"""

    allowed_delivery_modes: List[Literal["DIRECT", "BCC", "JOURNAL", "API", "RETRO_SCAN"]]

    created_at: datetime

    domain: str

    last_modified: datetime

    lookback_hops: int

    integration_id: Optional[str] = None

    o365_tenant_id: Optional[str] = None
