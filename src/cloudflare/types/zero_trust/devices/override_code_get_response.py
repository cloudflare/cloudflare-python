# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ...._models import BaseModel

__all__ = ["OverrideCodeGetResponse"]


class OverrideCodeGetResponse(BaseModel):
    disable_for_time: Optional[Dict[str, str]] = None
