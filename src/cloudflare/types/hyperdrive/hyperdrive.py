# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from .configuration import Configuration

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Hyperdrive", "Caching"]

class Caching(BaseModel):
    disabled: Optional[bool] = None
    """When set to true, disables the caching of SQL responses. (Default: false)"""

    max_age: Optional[int] = None
    """When present, specifies max duration for which items should persist in the
    cache.

    (Default: 60)
    """

    stale_while_revalidate: Optional[int] = None
    """
    When present, indicates the number of seconds cache may serve the response after
    it becomes stale. (Default: 15)
    """

class Hyperdrive(BaseModel):
    caching: Optional[Caching] = None

    name: Optional[str] = None

    origin: Optional[Configuration] = None