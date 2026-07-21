# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["GraphqlCreateResponse"]


class GraphqlCreateResponse(BaseModel):
    data: Optional[object] = None

    errors: Optional[List[object]] = None
