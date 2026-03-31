# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..rules.lists.list_cursor import ListCursor

__all__ = ["EnvironmentDeleteResponse", "Environment"]


class Environment(BaseModel):
    expression: str

    locked_on_deployment: Optional[bool] = None

    name: str

    position: ListCursor

    ref: str

    version: Optional[int] = None

    http_application_id: Optional[str] = None


class EnvironmentDeleteResponse(BaseModel):
    environments: List[Environment]
