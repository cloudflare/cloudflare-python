# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ....._models import BaseModel

__all__ = ["CADeleteResponse"]


class CADeleteResponse(BaseModel):
    id: Optional[str] = None
    """The ID of the CA."""
