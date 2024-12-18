# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["JobDeleteResponse"]


class JobDeleteResponse(BaseModel):
    id: Optional[int] = None
    """Unique id of the job."""
