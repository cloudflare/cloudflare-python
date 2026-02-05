# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OriginPostQuantumEncryptionGetResponse"]


class OriginPostQuantumEncryptionGetResponse(BaseModel):
    id: Literal["origin_pqe"]
    """The identifier of the caching setting."""

    editable: bool
    """Whether the setting is editable."""

    value: Literal["preferred", "supported", "off"]
    """Value of the Origin Post Quantum Encryption Setting."""

    modified_on: Optional[datetime] = None
    """Last time this setting was modified."""
