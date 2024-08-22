# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ServiceListResponse"]

class ServiceListResponse(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    name: Optional[str] = None
    """Name of a service running on the Cloudflare network"""