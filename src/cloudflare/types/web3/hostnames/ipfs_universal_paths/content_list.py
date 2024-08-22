# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

from typing import Optional

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ContentList"]

class ContentList(BaseModel):
    action: Optional[Literal["block"]] = None
    """Behavior of the content list."""