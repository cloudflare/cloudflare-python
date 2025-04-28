# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["ListDeleteResponse", "ID"]


class ID(BaseModel):
    id: Optional[str] = None
    """Defines the unique ID of the item in the List."""


ListDeleteResponse: TypeAlias = Union[ID, ID]
