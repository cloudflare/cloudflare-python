# File generated from our OpenAPI spec by Stainless.

from ..._models import BaseModel

__all__ = ["FilterUpdateResponse"]


class FilterUpdateResponse(BaseModel):
    id: str
    """Identifier"""

    enabled: bool

    pattern: str
