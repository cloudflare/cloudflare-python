# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UnnamedSchemaRef3"]


class UnnamedSchemaRef3(BaseModel):
    subscription_id: Optional[str] = None
    """Subscription identifier tag."""
