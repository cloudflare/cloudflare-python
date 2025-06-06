# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ScanCreateResponse", "Options"]


class Options(BaseModel):
    useragent: Optional[str] = None


class ScanCreateResponse(BaseModel):
    api: str
    """URL to api report."""

    message: str

    result: str
    """Public URL to report."""

    url: str
    """Canonical form of submitted URL. Use this if you want to later search by URL."""

    uuid: str
    """Scan ID."""

    visibility: Literal["public", "unlisted"]
    """Submitted visibility status."""

    options: Optional[Options] = None
