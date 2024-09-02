# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["IPV4Endpoint"]


class IPV4Endpoint(BaseModel):
    enabled: Optional[bool] = None
    """True if the endpoint is enabled for this location."""
