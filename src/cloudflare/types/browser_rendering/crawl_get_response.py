# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CrawlGetResponse", "Record", "RecordMetadata", "Robot"]


class RecordMetadata(BaseModel):
    """Absent for urls that never reached a fetch."""

    status: float
    """HTTP status code of the crawled page."""

    url: str
    """Final URL of the crawled page."""

    last_modified: Optional[str] = FieldInfo(alias="lastModified", default=None)
    """Value of the Last-Modified response header, when provided by the origin."""

    og_description: Optional[str] = FieldInfo(alias="og:description", default=None)
    """Open Graph description of the crawled page."""

    og_image: Optional[str] = FieldInfo(alias="og:image", default=None)
    """Open Graph image of the crawled page."""

    og_site_name: Optional[str] = FieldInfo(alias="og:site_name", default=None)
    """Open Graph site name of the crawled page."""

    og_title: Optional[str] = FieldInfo(alias="og:title", default=None)
    """Open Graph title of the crawled page."""

    og_type: Optional[str] = FieldInfo(alias="og:type", default=None)
    """Open Graph type of the crawled page."""

    title: Optional[str] = None
    """Title of the crawled page."""


class Record(BaseModel):
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

    metadata: Optional[RecordMetadata] = None
    """Absent for urls that never reached a fetch."""

    outcome: Optional[
        Literal[
            "success",
            "robots_disallowed",
            "crawl_purpose_disallowed",
            "content_use_disallowed",
            "connection_error",
            "timeout",
            "browser_unavailable",
            "format_generation_error",
            "unsupported_content_type",
            "unclassified_error",
            "page_error",
            "too_large",
        ]
    ] = None
    """Result of processing the URL. Absent for older records."""


class Robot(BaseModel):
    origin: str
    """Origin whose robots.txt was checked."""

    state: Literal["available", "absent", "fetch_failed"]
    """Whether usable robots.txt rules were available."""

    status: Optional[float] = None
    """HTTP status that established the current robots.txt state.

    Absent when no HTTP response was received.
    """


class CrawlGetResponse(BaseModel):
    id: str
    """Crawl job ID."""

    browser_seconds_used: float = FieldInfo(alias="browserSecondsUsed")
    """Total seconds spent in browser so far."""

    finished: float
    """Total number of URLs that have been crawled so far."""

    records: List[Record]
    """List of crawl job records."""

    robots: List[Robot]
    """Robots.txt state for the first 50 origins encountered by the crawl."""

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
