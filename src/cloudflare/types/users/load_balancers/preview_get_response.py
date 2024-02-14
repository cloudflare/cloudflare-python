# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List, Dict

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

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


PreviewGetResponse = Dict[str, PreviewGetResponseItem]
