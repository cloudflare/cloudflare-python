# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ProviderConfigListResponse"]


class ProviderConfigListResponse(BaseModel):
    id: str

    account_id: str

    account_tag: str

    alias: str

    default_config: bool

    gateway_id: str
    """gateway id"""

    modified_at: datetime

    provider_slug: str

    secret_id: str

    secret_preview: str

    rate_limit: Optional[float] = None

    rate_limit_period: Optional[float] = None
