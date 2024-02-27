# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CfInterconnectUpdateResponse"]


class CfInterconnectUpdateResponse(BaseModel):
    modified: Optional[bool] = None

    modified_interconnect: Optional[object] = None
