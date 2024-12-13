# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MXRecord"]


class MXRecord(BaseModel):
    content: Optional[str] = None
    """A valid mail server hostname."""

    priority: Optional[float] = None
    """Required for MX, SRV and URI records; unused by other record types.

    Records with lower priorities are preferred.
    """

    type: Optional[Literal["MX"]] = None
    """Record type."""
