# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AIGatewayGetResponse"]


class AIGatewayGetResponse(BaseModel):
    id: str
    """gateway id"""

    account_id: str

    account_tag: str

    cache_invalidate_on_update: bool

    cache_ttl: Optional[int] = None

    collect_logs: bool

    created_at: datetime

    internal_id: str

    modified_at: datetime

    rate_limiting_interval: Optional[int] = None

    rate_limiting_limit: Optional[int] = None

    rate_limiting_technique: Literal["fixed", "sliding"]

    authentication: Optional[bool] = None

    log_management: Optional[int] = None

    log_management_strategy: Optional[Literal["STOP_INSERTING", "DELETE_OLDEST"]] = None

    logpush: Optional[bool] = None

    logpush_public_key: Optional[str] = None
