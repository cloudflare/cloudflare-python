# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ......_models import BaseModel

__all__ = ["LogGetResponse", "Data"]


class Data(BaseModel):
    line: Optional[str] = None

    ts: Optional[str] = None


class LogGetResponse(BaseModel):
    data: Optional[List[Data]] = None

    includes_container_logs: Optional[bool] = None

    total: Optional[int] = None
