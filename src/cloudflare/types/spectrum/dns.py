# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["DNS"]

class DNS(BaseModel):
    name: Optional[str] = None
    """The name of the DNS record associated with the application."""

    type: Optional[Literal["CNAME", "ADDRESS"]] = None
    """The type of DNS record associated with the application."""