# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Namespace"]


class Namespace(BaseModel):
    id: Optional[object] = None

    class_: Optional[object] = FieldInfo(alias="class", default=None)

    name: Optional[object] = None

    script: Optional[object] = None
