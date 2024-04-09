# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ...._models import BaseModel

__all__ = ["Preview", "PreviewItem", "PreviewItemOriginPreviewItemOriginItem"]


class PreviewItemOriginPreviewItemOriginItem(BaseModel):
    failure_reason: Optional[str] = None

    healthy: Optional[bool] = None

    response_code: Optional[float] = None

    rtt: Optional[str] = None


class PreviewItem(BaseModel):
    healthy: Optional[bool] = None

    origins: Optional[List[Dict[str, PreviewItemOriginPreviewItemOriginItem]]] = None


Preview = Dict[str, PreviewItem]
