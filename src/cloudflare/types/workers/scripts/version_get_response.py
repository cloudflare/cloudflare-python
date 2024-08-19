# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["VersionGetResponse"]


class VersionGetResponse(BaseModel):
    resources: object

    id: Optional[str] = None

    metadata: Optional[object] = None

    number: Optional[float] = None
