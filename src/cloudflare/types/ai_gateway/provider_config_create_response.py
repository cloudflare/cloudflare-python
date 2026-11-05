# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime

from ..._models import BaseModel

__all__ = ["ProviderConfigCreateResponse"]


class ProviderConfigCreateResponse(BaseModel):
    id: str

    alias: str

    default_config: bool

    gateway_id: str
    """Unique identifier of the AI Gateway within the account."""

    modified_at: datetime

    provider_slug: str

    secret_id: str

    secret_preview: str

    last_used_at: Optional[date] = None
    """
    UTC date (YYYY-MM-DD) the gateway last selected this key to authenticate a
    request to the provider, whether or not the request succeeded. Updated at most
    once a day. Null if the gateway has not used the key since this field was
    introduced.
    """

    rate_limit: Optional[float] = None

    rate_limit_period: Optional[float] = None
