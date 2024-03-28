# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ...._models import BaseModel

__all__ = [
    "LoadBalancingPreview",
    "LoadBalancingPreviewItem",
    "LoadBalancingPreviewItemOriginLoadBalancingPreviewItemOriginItem",
]


class LoadBalancingPreviewItemOriginLoadBalancingPreviewItemOriginItem(BaseModel):
    failure_reason: Optional[str] = None

    healthy: Optional[bool] = None

    response_code: Optional[float] = None

    rtt: Optional[str] = None


class LoadBalancingPreviewItem(BaseModel):
    healthy: Optional[bool] = None

    origins: Optional[List[Dict[str, LoadBalancingPreviewItemOriginLoadBalancingPreviewItemOriginItem]]] = None


LoadBalancingPreview = Dict[str, LoadBalancingPreviewItem]
