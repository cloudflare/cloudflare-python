# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TransformerDeleteResponse"]


class TransformerDeleteResponse(BaseModel):
    id: Optional[int] = None
    """The deleted transformer's ID."""
