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
from .json import (
    JsonResource,
    AsyncJsonResource,
    JsonResourceWithRawResponse,
    AsyncJsonResourceWithRawResponse,
    JsonResourceWithStreamingResponse,
    AsyncJsonResourceWithStreamingResponse,
)
from .links import (
    LinksResource,
    AsyncLinksResource,
    LinksResourceWithRawResponse,
    AsyncLinksResourceWithRawResponse,
    LinksResourceWithStreamingResponse,
    AsyncLinksResourceWithStreamingResponse,
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
from .markdown import (
    MarkdownResource,
    AsyncMarkdownResource,
    MarkdownResourceWithRawResponse,
    AsyncMarkdownResourceWithRawResponse,
    MarkdownResourceWithStreamingResponse,
    AsyncMarkdownResourceWithStreamingResponse,
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

__all__ = ["BrowserRenderingResource", "AsyncBrowserRenderingResource"]


class BrowserRenderingResource(SyncAPIResource):
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
    def json(self) -> JsonResource:
        return JsonResource(self._client)

    @cached_property
    def links(self) -> LinksResource:
        return LinksResource(self._client)

    @cached_property
    def markdown(self) -> MarkdownResource:
        return MarkdownResource(self._client)

    @cached_property
    def with_raw_response(self) -> BrowserRenderingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return BrowserRenderingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrowserRenderingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return BrowserRenderingResourceWithStreamingResponse(self)


class AsyncBrowserRenderingResource(AsyncAPIResource):
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
    def json(self) -> AsyncJsonResource:
        return AsyncJsonResource(self._client)

    @cached_property
    def links(self) -> AsyncLinksResource:
        return AsyncLinksResource(self._client)

    @cached_property
    def markdown(self) -> AsyncMarkdownResource:
        return AsyncMarkdownResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBrowserRenderingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBrowserRenderingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrowserRenderingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncBrowserRenderingResourceWithStreamingResponse(self)


class BrowserRenderingResourceWithRawResponse:
    def __init__(self, browser_rendering: BrowserRenderingResource) -> None:
        self._browser_rendering = browser_rendering

    @cached_property
    def content(self) -> ContentResourceWithRawResponse:
        return ContentResourceWithRawResponse(self._browser_rendering.content)

    @cached_property
    def pdf(self) -> PDFResourceWithRawResponse:
        return PDFResourceWithRawResponse(self._browser_rendering.pdf)

    @cached_property
    def scrape(self) -> ScrapeResourceWithRawResponse:
        return ScrapeResourceWithRawResponse(self._browser_rendering.scrape)

    @cached_property
    def screenshot(self) -> ScreenshotResourceWithRawResponse:
        return ScreenshotResourceWithRawResponse(self._browser_rendering.screenshot)

    @cached_property
    def snapshot(self) -> SnapshotResourceWithRawResponse:
        return SnapshotResourceWithRawResponse(self._browser_rendering.snapshot)

    @cached_property
    def json(self) -> JsonResourceWithRawResponse:
        return JsonResourceWithRawResponse(self._browser_rendering.json)

    @cached_property
    def links(self) -> LinksResourceWithRawResponse:
        return LinksResourceWithRawResponse(self._browser_rendering.links)

    @cached_property
    def markdown(self) -> MarkdownResourceWithRawResponse:
        return MarkdownResourceWithRawResponse(self._browser_rendering.markdown)


class AsyncBrowserRenderingResourceWithRawResponse:
    def __init__(self, browser_rendering: AsyncBrowserRenderingResource) -> None:
        self._browser_rendering = browser_rendering

    @cached_property
    def content(self) -> AsyncContentResourceWithRawResponse:
        return AsyncContentResourceWithRawResponse(self._browser_rendering.content)

    @cached_property
    def pdf(self) -> AsyncPDFResourceWithRawResponse:
        return AsyncPDFResourceWithRawResponse(self._browser_rendering.pdf)

    @cached_property
    def scrape(self) -> AsyncScrapeResourceWithRawResponse:
        return AsyncScrapeResourceWithRawResponse(self._browser_rendering.scrape)

    @cached_property
    def screenshot(self) -> AsyncScreenshotResourceWithRawResponse:
        return AsyncScreenshotResourceWithRawResponse(self._browser_rendering.screenshot)

    @cached_property
    def snapshot(self) -> AsyncSnapshotResourceWithRawResponse:
        return AsyncSnapshotResourceWithRawResponse(self._browser_rendering.snapshot)

    @cached_property
    def json(self) -> AsyncJsonResourceWithRawResponse:
        return AsyncJsonResourceWithRawResponse(self._browser_rendering.json)

    @cached_property
    def links(self) -> AsyncLinksResourceWithRawResponse:
        return AsyncLinksResourceWithRawResponse(self._browser_rendering.links)

    @cached_property
    def markdown(self) -> AsyncMarkdownResourceWithRawResponse:
        return AsyncMarkdownResourceWithRawResponse(self._browser_rendering.markdown)


class BrowserRenderingResourceWithStreamingResponse:
    def __init__(self, browser_rendering: BrowserRenderingResource) -> None:
        self._browser_rendering = browser_rendering

    @cached_property
    def content(self) -> ContentResourceWithStreamingResponse:
        return ContentResourceWithStreamingResponse(self._browser_rendering.content)

    @cached_property
    def pdf(self) -> PDFResourceWithStreamingResponse:
        return PDFResourceWithStreamingResponse(self._browser_rendering.pdf)

    @cached_property
    def scrape(self) -> ScrapeResourceWithStreamingResponse:
        return ScrapeResourceWithStreamingResponse(self._browser_rendering.scrape)

    @cached_property
    def screenshot(self) -> ScreenshotResourceWithStreamingResponse:
        return ScreenshotResourceWithStreamingResponse(self._browser_rendering.screenshot)

    @cached_property
    def snapshot(self) -> SnapshotResourceWithStreamingResponse:
        return SnapshotResourceWithStreamingResponse(self._browser_rendering.snapshot)

    @cached_property
    def json(self) -> JsonResourceWithStreamingResponse:
        return JsonResourceWithStreamingResponse(self._browser_rendering.json)

    @cached_property
    def links(self) -> LinksResourceWithStreamingResponse:
        return LinksResourceWithStreamingResponse(self._browser_rendering.links)

    @cached_property
    def markdown(self) -> MarkdownResourceWithStreamingResponse:
        return MarkdownResourceWithStreamingResponse(self._browser_rendering.markdown)


class AsyncBrowserRenderingResourceWithStreamingResponse:
    def __init__(self, browser_rendering: AsyncBrowserRenderingResource) -> None:
        self._browser_rendering = browser_rendering

    @cached_property
    def content(self) -> AsyncContentResourceWithStreamingResponse:
        return AsyncContentResourceWithStreamingResponse(self._browser_rendering.content)

    @cached_property
    def pdf(self) -> AsyncPDFResourceWithStreamingResponse:
        return AsyncPDFResourceWithStreamingResponse(self._browser_rendering.pdf)

    @cached_property
    def scrape(self) -> AsyncScrapeResourceWithStreamingResponse:
        return AsyncScrapeResourceWithStreamingResponse(self._browser_rendering.scrape)

    @cached_property
    def screenshot(self) -> AsyncScreenshotResourceWithStreamingResponse:
        return AsyncScreenshotResourceWithStreamingResponse(self._browser_rendering.screenshot)

    @cached_property
    def snapshot(self) -> AsyncSnapshotResourceWithStreamingResponse:
        return AsyncSnapshotResourceWithStreamingResponse(self._browser_rendering.snapshot)

    @cached_property
    def json(self) -> AsyncJsonResourceWithStreamingResponse:
        return AsyncJsonResourceWithStreamingResponse(self._browser_rendering.json)

    @cached_property
    def links(self) -> AsyncLinksResourceWithStreamingResponse:
        return AsyncLinksResourceWithStreamingResponse(self._browser_rendering.links)

    @cached_property
    def markdown(self) -> AsyncMarkdownResourceWithStreamingResponse:
        return AsyncMarkdownResourceWithStreamingResponse(self._browser_rendering.markdown)
