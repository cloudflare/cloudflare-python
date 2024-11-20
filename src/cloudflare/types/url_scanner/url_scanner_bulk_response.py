# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["URLScannerBulkResponse", "URLScannerBulkResponseItem", "URLScannerBulkResponseItemOptions"]


class URLScannerBulkResponseItemOptions(BaseModel):
    useragent: Optional[str] = None


class URLScannerBulkResponseItem(BaseModel):
    api: str
    """URL to api report."""

    result: str
    """URL to report."""

    url: str
    """Submitted URL"""

    uuid: str
    """Scan ID."""

    visibility: str
    """Submitted visibility status."""

    options: Optional[URLScannerBulkResponseItemOptions] = None


URLScannerBulkResponse: TypeAlias = List[URLScannerBulkResponseItem]
