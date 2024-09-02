# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Namespace"]


class Namespace(BaseModel):
    id: Optional[str] = None

    class_: Optional[str] = FieldInfo(alias="class", default=None)

    name: Optional[str] = None

    script: Optional[str] = None
