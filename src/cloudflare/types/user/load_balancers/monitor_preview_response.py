# File generated from our OpenAPI spec by Stainless.

from typing import Dict, Optional

from ...._models import BaseModel

__all__ = ["MonitorPreviewResponse"]


class MonitorPreviewResponse(BaseModel):
    pools: Optional[Dict[str, str]] = None
    """Monitored pool IDs mapped to their respective names."""

    preview_id: Optional[str] = None
