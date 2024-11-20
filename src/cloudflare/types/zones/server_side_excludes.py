# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ServerSideExcludes"]


class ServerSideExcludes(BaseModel):
    id: Optional[Literal["server_side_exclude"]] = None
