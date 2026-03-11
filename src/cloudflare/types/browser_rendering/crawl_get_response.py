# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CrawlGetResponse", "Record", "RecordMetadata"]


class RecordMetadata(BaseModel):
    status: float
    """HTTP status code of the crawled page."""

    url: str
    """Final URL of the crawled page."""

    title: Optional[str] = None
    """Title of the crawled page."""


class Record(BaseModel):
    metadata: RecordMetadata

    status: Literal["queued", "errored", "completed", "disallowed", "skipped", "cancelled"]
    """Current status of the crawled URL."""

    url: str
    """Crawled URL."""

    html: Optional[str] = None
    """HTML content of the crawled URL."""

    json_: Optional[Dict[str, Optional[object]]] = FieldInfo(alias="json", default=None)
    """JSON of the content of the crawled URL."""

    markdown: Optional[str] = None
    """Markdown of the content of the crawled URL."""


class CrawlGetResponse(BaseModel):
    id: str
    """Crawl job ID."""

    browser_seconds_used: float = FieldInfo(alias="browserSecondsUsed")
    """Total seconds spent in browser so far."""

    finished: float
    """Total number of URLs that have been crawled so far."""

    records: List[Record]
    """List of crawl job records."""

    skipped: float
    """Total number of URLs that were skipped due to include/exclude/subdomain filters.

    Skipped URLs are included in records but are not counted toward total/finished.
    """

    status: str
    """Current crawl job status."""

    total: float
    """Total current number of URLs in the crawl job."""

    cursor: Optional[str] = None
    """Cursor for pagination."""
