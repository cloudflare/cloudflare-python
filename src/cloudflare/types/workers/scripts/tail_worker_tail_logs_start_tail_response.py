# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["TailWorkerTailLogsStartTailResponse"]


class TailWorkerTailLogsStartTailResponse(BaseModel):
    id: Optional[object] = None

    expires_at: Optional[object] = None

    url: Optional[object] = None
