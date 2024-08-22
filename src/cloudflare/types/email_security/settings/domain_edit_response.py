# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["DomainEditResponse"]


class DomainEditResponse(BaseModel):
    id: int
    """Unique domain identifier"""

    allowed_delivery_modes: List[Literal["DIRECT", "BCC", "JOURNAL", "API", "RETRO_SCAN"]]

    created_at: datetime

    domain: str

    last_modified: datetime

    lookback_hops: int

    integration_id: Optional[str] = None

    o365_tenant_id: Optional[str] = None
