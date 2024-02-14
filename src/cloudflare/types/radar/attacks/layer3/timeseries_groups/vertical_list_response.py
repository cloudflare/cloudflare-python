# File generated from our OpenAPI spec by Stainless.

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ......_models import BaseModel
from ......types import shared
from typing import TYPE_CHECKING

__all__ = ["VerticalListResponse", "Serie0"]


class Serie0(BaseModel):
    timestamps: List[str]

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> List[str]:
            ...


class VerticalListResponse(BaseModel):
    meta: object

    serie_0: Serie0
