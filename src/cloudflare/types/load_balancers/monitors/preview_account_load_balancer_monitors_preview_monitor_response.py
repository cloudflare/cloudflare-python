# File generated from our OpenAPI spec by Stainless.

from typing import Optional, Dict

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["PreviewAccountLoadBalancerMonitorsPreviewMonitorResponse"]


class PreviewAccountLoadBalancerMonitorsPreviewMonitorResponse(BaseModel):
    pools: Optional[Dict[str, str]] = None
    """Monitored pool IDs mapped to their respective names."""

    preview_id: Optional[str] = None
