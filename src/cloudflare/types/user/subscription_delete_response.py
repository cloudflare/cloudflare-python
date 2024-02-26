# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SubscriptionDeleteResponse"]


class SubscriptionDeleteResponse(BaseModel):
    subscription_id: Optional[str] = None
    """Subscription identifier tag."""
