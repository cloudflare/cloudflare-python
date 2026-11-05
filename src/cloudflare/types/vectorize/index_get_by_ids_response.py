# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["IndexGetByIDsResponse"]


class IndexGetByIDsResponse(BaseModel):
    id: Optional[str] = None
    """Identifier for a Vector"""

    metadata: Optional[object] = None

    namespace: Optional[str] = None

    values: Optional[List[float]] = None
