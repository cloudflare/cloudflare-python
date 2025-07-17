# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["BrandProtectionSubmitResponse"]


class BrandProtectionSubmitResponse(BaseModel):
    skipped_urls: Optional[List[Dict[str, object]]] = None

    submitted_urls: Optional[List[Dict[str, object]]] = None
