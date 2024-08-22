# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from datetime import datetime

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["VirtualNetwork"]

class VirtualNetwork(BaseModel):
    id: str
    """UUID of the virtual network."""

    comment: str
    """Optional remark describing the virtual network."""

    created_at: datetime
    """Timestamp of when the resource was created."""

    is_default_network: bool
    """If `true`, this virtual network is the default for the account."""

    name: str
    """A user-friendly name for the virtual network."""

    deleted_at: Optional[datetime] = None
    """Timestamp of when the resource was deleted.

    If `null`, the resource has not been deleted.
    """