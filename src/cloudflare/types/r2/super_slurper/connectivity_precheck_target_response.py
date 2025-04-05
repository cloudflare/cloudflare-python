# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ConnectivityPrecheckTargetResponse"]


class ConnectivityPrecheckTargetResponse(BaseModel):
    connectivity_status: Optional[Literal["success", "error"]] = FieldInfo(alias="connectivityStatus", default=None)
