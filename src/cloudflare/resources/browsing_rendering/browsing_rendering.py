# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .pdf import (
    PDFResource,
    AsyncPDFResource,
    PDFResourceWithRawResponse,
    AsyncPDFResourceWithRawResponse,
    PDFResourceWithStreamingResponse,
    AsyncPDFResourceWithStreamingResponse,
)
from .scrape import (
    ScrapeResource,
    AsyncScrapeResource,
    ScrapeResourceWithRawResponse,
    AsyncScrapeResourceWithRawResponse,
    ScrapeResourceWithStreamingResponse,
    AsyncScrapeResourceWithStreamingResponse,
)
from .content import (
    ContentResource,
    AsyncContentResource,
    ContentResourceWithRawResponse,
    AsyncContentResourceWithRawResponse,
    ContentResourceWithStreamingResponse,
    AsyncContentResourceWithStreamingResponse,
)
from .snapshot import (
    SnapshotResource,
    AsyncSnapshotResource,
    SnapshotResourceWithRawResponse,
    AsyncSnapshotResourceWithRawResponse,
    SnapshotResourceWithStreamingResponse,
    AsyncSnapshotResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .screenshot import (
    ScreenshotResource,
    AsyncScreenshotResource,
    ScreenshotResourceWithRawResponse,
    AsyncScreenshotResourceWithRawResponse,
    ScreenshotResourceWithStreamingResponse,
    AsyncScreenshotResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["BrowsingRenderingResource", "AsyncBrowsingRenderingResource"]


class BrowsingRenderingResource(SyncAPIResource):
    @cached_property
    def content(self) -> ContentResource:
        return ContentResource(self._client)

    @cached_property
    def pdf(self) -> PDFResource:
        return PDFResource(self._client)

    @cached_property
    def scrape(self) -> ScrapeResource:
        return ScrapeResource(self._client)

    @cached_property
    def screenshot(self) -> ScreenshotResource:
        return ScreenshotResource(self._client)

    @cached_property
    def snapshot(self) -> SnapshotResource:
        return SnapshotResource(self._client)

    @cached_property
    def with_raw_response(self) -> BrowsingRenderingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return BrowsingRenderingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrowsingRenderingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return BrowsingRenderingResourceWithStreamingResponse(self)


class AsyncBrowsingRenderingResource(AsyncAPIResource):
    @cached_property
    def content(self) -> AsyncContentResource:
        return AsyncContentResource(self._client)

    @cached_property
    def pdf(self) -> AsyncPDFResource:
        return AsyncPDFResource(self._client)

    @cached_property
    def scrape(self) -> AsyncScrapeResource:
        return AsyncScrapeResource(self._client)

    @cached_property
    def screenshot(self) -> AsyncScreenshotResource:
        return AsyncScreenshotResource(self._client)

    @cached_property
    def snapshot(self) -> AsyncSnapshotResource:
        return AsyncSnapshotResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBrowsingRenderingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBrowsingRenderingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrowsingRenderingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncBrowsingRenderingResourceWithStreamingResponse(self)


class BrowsingRenderingResourceWithRawResponse:
    def __init__(self, browsing_rendering: BrowsingRenderingResource) -> None:
        self._browsing_rendering = browsing_rendering

    @cached_property
    def content(self) -> ContentResourceWithRawResponse:
        return ContentResourceWithRawResponse(self._browsing_rendering.content)

    @cached_property
    def pdf(self) -> PDFResourceWithRawResponse:
        return PDFResourceWithRawResponse(self._browsing_rendering.pdf)

    @cached_property
    def scrape(self) -> ScrapeResourceWithRawResponse:
        return ScrapeResourceWithRawResponse(self._browsing_rendering.scrape)

    @cached_property
    def screenshot(self) -> ScreenshotResourceWithRawResponse:
        return ScreenshotResourceWithRawResponse(self._browsing_rendering.screenshot)

    @cached_property
    def snapshot(self) -> SnapshotResourceWithRawResponse:
        return SnapshotResourceWithRawResponse(self._browsing_rendering.snapshot)


class AsyncBrowsingRenderingResourceWithRawResponse:
    def __init__(self, browsing_rendering: AsyncBrowsingRenderingResource) -> None:
        self._browsing_rendering = browsing_rendering

    @cached_property
    def content(self) -> AsyncContentResourceWithRawResponse:
        return AsyncContentResourceWithRawResponse(self._browsing_rendering.content)

    @cached_property
    def pdf(self) -> AsyncPDFResourceWithRawResponse:
        return AsyncPDFResourceWithRawResponse(self._browsing_rendering.pdf)

    @cached_property
    def scrape(self) -> AsyncScrapeResourceWithRawResponse:
        return AsyncScrapeResourceWithRawResponse(self._browsing_rendering.scrape)

    @cached_property
    def screenshot(self) -> AsyncScreenshotResourceWithRawResponse:
        return AsyncScreenshotResourceWithRawResponse(self._browsing_rendering.screenshot)

    @cached_property
    def snapshot(self) -> AsyncSnapshotResourceWithRawResponse:
        return AsyncSnapshotResourceWithRawResponse(self._browsing_rendering.snapshot)


class BrowsingRenderingResourceWithStreamingResponse:
    def __init__(self, browsing_rendering: BrowsingRenderingResource) -> None:
        self._browsing_rendering = browsing_rendering

    @cached_property
    def content(self) -> ContentResourceWithStreamingResponse:
        return ContentResourceWithStreamingResponse(self._browsing_rendering.content)

    @cached_property
    def pdf(self) -> PDFResourceWithStreamingResponse:
        return PDFResourceWithStreamingResponse(self._browsing_rendering.pdf)

    @cached_property
    def scrape(self) -> ScrapeResourceWithStreamingResponse:
        return ScrapeResourceWithStreamingResponse(self._browsing_rendering.scrape)

    @cached_property
    def screenshot(self) -> ScreenshotResourceWithStreamingResponse:
        return ScreenshotResourceWithStreamingResponse(self._browsing_rendering.screenshot)

    @cached_property
    def snapshot(self) -> SnapshotResourceWithStreamingResponse:
        return SnapshotResourceWithStreamingResponse(self._browsing_rendering.snapshot)


class AsyncBrowsingRenderingResourceWithStreamingResponse:
    def __init__(self, browsing_rendering: AsyncBrowsingRenderingResource) -> None:
        self._browsing_rendering = browsing_rendering

    @cached_property
    def content(self) -> AsyncContentResourceWithStreamingResponse:
        return AsyncContentResourceWithStreamingResponse(self._browsing_rendering.content)

    @cached_property
    def pdf(self) -> AsyncPDFResourceWithStreamingResponse:
        return AsyncPDFResourceWithStreamingResponse(self._browsing_rendering.pdf)

    @cached_property
    def scrape(self) -> AsyncScrapeResourceWithStreamingResponse:
        return AsyncScrapeResourceWithStreamingResponse(self._browsing_rendering.scrape)

    @cached_property
    def screenshot(self) -> AsyncScreenshotResourceWithStreamingResponse:
        return AsyncScreenshotResourceWithStreamingResponse(self._browsing_rendering.screenshot)

    @cached_property
    def snapshot(self) -> AsyncSnapshotResourceWithStreamingResponse:
        return AsyncSnapshotResourceWithStreamingResponse(self._browsing_rendering.snapshot)
