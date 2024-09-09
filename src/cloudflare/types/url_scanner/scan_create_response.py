# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["ScanCreateResponse"]


class ScanCreateResponse(BaseModel):
    time: datetime
    """Time when url was submitted for scanning."""

    url: str
    """Canonical form of submitted URL. Use this if you want to later search by URL."""

    uuid: str
    """Scan ID."""

    visibility: str
    """Submitted visibility status."""
