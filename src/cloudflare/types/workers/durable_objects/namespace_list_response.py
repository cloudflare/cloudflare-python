# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["NamespaceListResponse", "NamespaceListResponseItem"]


class NamespaceListResponseItem(BaseModel):
    id: Optional[object] = None

    class_: Optional[object] = FieldInfo(alias="class", default=None)

    name: Optional[object] = None

    script: Optional[object] = None


NamespaceListResponse = List[NamespaceListResponseItem]
