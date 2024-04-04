# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from .unnamed_schema_ref_b234e6a28c1a1c7c29213787c0621eaa import UnnamedSchemaRefB234e6a28c1a1c7c29213787c0621eaa

__all__ = ["OriginMaxHTTPVersionGetResponse"]


class OriginMaxHTTPVersionGetResponse(BaseModel):
    id: UnnamedSchemaRefB234e6a28c1a1c7c29213787c0621eaa
    """Value of the zone setting."""

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""

    value: Literal["2", "1"]
    """Value of the Origin Max HTTP Version Setting."""
