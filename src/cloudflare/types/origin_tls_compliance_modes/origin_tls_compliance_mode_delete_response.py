# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OriginTLSComplianceModeDeleteResponse"]


class OriginTLSComplianceModeDeleteResponse(BaseModel):
    id: Literal["origin_tls_compliance_modes"]
    """The identifier of the caching setting."""

    editable: bool
    """Whether the setting is editable."""

    modified_on: Optional[datetime] = None
    """Last time this setting was modified."""
