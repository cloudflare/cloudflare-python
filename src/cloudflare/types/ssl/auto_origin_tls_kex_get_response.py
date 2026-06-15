# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["AutoOriginTLSKexGetResponse"]


class AutoOriginTLSKexGetResponse(BaseModel):
    id: str

    enabled: bool
    """Whether Auto-Origin TLS KEX selection is enabled for the zone."""

    modified_on: datetime
    """Last time this setting was modified."""
