# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ......_models import BaseModel

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["LogGetResponse", "Data"]


class Data(BaseModel):
    line: Optional[str] = None

    ts: Optional[str] = None


class LogGetResponse(BaseModel):
    data: Optional[List[Data]] = None

    includes_container_logs: Optional[bool] = None

    total: Optional[int] = None
