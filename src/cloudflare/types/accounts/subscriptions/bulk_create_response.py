# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ...shared.subscription import Subscription

__all__ = ["BulkCreateResponse"]


class BulkCreateResponse(BaseModel):
    client_secrets: Optional[List[str]] = None

    subscriptions: Optional[List[Subscription]] = None
