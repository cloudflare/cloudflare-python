# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UaRuleDeleteResponse"]


class UaRuleDeleteResponse(BaseModel):
    id: Optional[str] = None
    """The unique identifier of the User Agent Blocking rule."""
