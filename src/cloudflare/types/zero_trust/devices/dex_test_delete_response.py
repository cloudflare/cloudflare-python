# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .schema_http import SchemaHTTP

__all__ = ["DEXTestDeleteResponse"]


class DEXTestDeleteResponse(BaseModel):
    dex_tests: Optional[List[SchemaHTTP]] = None
