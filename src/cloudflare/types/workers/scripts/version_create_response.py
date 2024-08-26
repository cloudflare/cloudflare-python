# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["VersionCreateResponse"]


class VersionCreateResponse(BaseModel):
    resources: object

    id: Optional[str] = None

    metadata: Optional[object] = None

    number: Optional[float] = None

    startup_time_ms: Optional[int] = None
