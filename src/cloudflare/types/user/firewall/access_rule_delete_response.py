# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ...._models import BaseModel

__all__ = ["AccessRuleDeleteResponse"]


class AccessRuleDeleteResponse(BaseModel):
    id: Optional[str] = None
    """The unique identifier of the IP Access rule."""
