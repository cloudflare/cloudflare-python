# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from datetime import datetime

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["AIGatewayListResponse"]

class AIGatewayListResponse(BaseModel):
    id: str
    """gateway id"""

    cache_invalidate_on_update: bool

    cache_ttl: Optional[int] = None

    collect_logs: bool

    created_at: datetime

    modified_at: datetime

    rate_limiting_interval: Optional[int] = None

    rate_limiting_limit: Optional[int] = None

    rate_limiting_technique: Literal["fixed", "sliding"]