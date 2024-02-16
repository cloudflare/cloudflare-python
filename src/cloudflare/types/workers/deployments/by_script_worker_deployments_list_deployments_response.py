# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["ByScriptWorkerDeploymentsListDeploymentsResponse"]


class ByScriptWorkerDeploymentsListDeploymentsResponse(BaseModel):
    items: Optional[List[object]] = None

    latest: Optional[object] = None
