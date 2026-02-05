# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["LogoMatchDownloadResponse"]


class LogoMatchDownloadResponse(BaseModel):
    matches: Optional[List[Dict[str, object]]] = None

    total: Optional[int] = None
