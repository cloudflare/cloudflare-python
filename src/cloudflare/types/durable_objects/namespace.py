# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Namespace"]


class Namespace(BaseModel):
    id: Optional[str] = None

    class_: Optional[str] = FieldInfo(alias="class", default=None)

    name: Optional[str] = None

    script: Optional[str] = None

    use_sqlite: Optional[bool] = None
