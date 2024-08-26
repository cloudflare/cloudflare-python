# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = [
    "PreviewGetResponse",
    "PreviewGetResponseItem",
    "PreviewGetResponseItemOriginPreviewGetResponseItemOriginItem",
]


class PreviewGetResponseItemOriginPreviewGetResponseItemOriginItem(BaseModel):
    failure_reason: Optional[str] = None

    healthy: Optional[bool] = None

    response_code: Optional[float] = None

    rtt: Optional[str] = None


class PreviewGetResponseItem(BaseModel):
    healthy: Optional[bool] = None

    origins: Optional[List[Dict[str, PreviewGetResponseItemOriginPreviewGetResponseItemOriginItem]]] = None


PreviewGetResponse: TypeAlias = Dict[str, PreviewGetResponseItem]
