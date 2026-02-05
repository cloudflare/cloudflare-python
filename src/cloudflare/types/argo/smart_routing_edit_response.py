# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SmartRoutingEditResponse"]


class SmartRoutingEditResponse(BaseModel):
    id: str
    """Specifies the identifier of the Argo Smart Routing setting."""

    editable: bool
    """Specifies if the setting is editable."""

    value: Literal["on", "off"]
    """Specifies the enablement value of Argo Smart Routing."""

    modified_on: Optional[datetime] = None
    """Specifies the time when the setting was last modified."""
