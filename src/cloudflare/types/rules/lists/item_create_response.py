# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["ItemCreateResponse", "OperationID"]


class OperationID(BaseModel):
    operation_id: Optional[str] = None
    """The unique operation ID of the asynchronous action."""


ItemCreateResponse: TypeAlias = Union[OperationID, OperationID]
