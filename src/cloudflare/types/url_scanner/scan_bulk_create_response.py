# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["ScanBulkCreateResponse", "ScanBulkCreateResponseItem", "ScanBulkCreateResponseItemOptions"]


class ScanBulkCreateResponseItemOptions(BaseModel):
    useragent: Optional[str] = None


class ScanBulkCreateResponseItem(BaseModel):
    api: str
    """URL to api report."""

    result: str
    """URL to report."""

    url: str
    """Submitted URL"""

    uuid: str
    """Scan ID."""

    visibility: Literal["public", "unlisted"]
    """Submitted visibility status."""

    options: Optional[ScanBulkCreateResponseItemOptions] = None


ScanBulkCreateResponse: TypeAlias = List[ScanBulkCreateResponseItem]
