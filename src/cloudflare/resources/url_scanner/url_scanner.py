# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .dom import (
    DomResource,
    AsyncDomResource,
    DomResourceWithRawResponse,
    AsyncDomResourceWithRawResponse,
    DomResourceWithStreamingResponse,
    AsyncDomResourceWithStreamingResponse,
)
from .har import (
    HarResource,
    AsyncHarResource,
    HarResourceWithRawResponse,
    AsyncHarResourceWithRawResponse,
    HarResourceWithStreamingResponse,
    AsyncHarResourceWithStreamingResponse,
)
from .scans import (
    ScansResource,
    AsyncScansResource,
    ScansResourceWithRawResponse,
    AsyncScansResourceWithRawResponse,
    ScansResourceWithStreamingResponse,
    AsyncScansResourceWithStreamingResponse,
)
from .result import (
    ResultResource,
    AsyncResultResource,
    ResultResourceWithRawResponse,
    AsyncResultResourceWithRawResponse,
    ResultResourceWithStreamingResponse,
    AsyncResultResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .responses import (
    ResponsesResource,
    AsyncResponsesResource,
    ResponsesResourceWithRawResponse,
    AsyncResponsesResourceWithRawResponse,
    ResponsesResourceWithStreamingResponse,
    AsyncResponsesResourceWithStreamingResponse,
)
from .screenshot import (
    ScreenshotResource,
    AsyncScreenshotResource,
    ScreenshotResourceWithRawResponse,
    AsyncScreenshotResourceWithRawResponse,
    ScreenshotResourceWithStreamingResponse,
    AsyncScreenshotResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["URLScannerResource", "AsyncURLScannerResource"]


class URLScannerResource(SyncAPIResource):
    @cached_property
    def responses(self) -> ResponsesResource:
        return ResponsesResource(self._client)

    @cached_property
    def scans(self) -> ScansResource:
        return ScansResource(self._client)

    @cached_property
    def dom(self) -> DomResource:
        return DomResource(self._client)

    @cached_property
    def har(self) -> HarResource:
        return HarResource(self._client)

    @cached_property
    def result(self) -> ResultResource:
        return ResultResource(self._client)

    @cached_property
    def screenshot(self) -> ScreenshotResource:
        return ScreenshotResource(self._client)

    @cached_property
    def with_raw_response(self) -> URLScannerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return URLScannerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> URLScannerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return URLScannerResourceWithStreamingResponse(self)


class AsyncURLScannerResource(AsyncAPIResource):
    @cached_property
    def responses(self) -> AsyncResponsesResource:
        return AsyncResponsesResource(self._client)

    @cached_property
    def scans(self) -> AsyncScansResource:
        return AsyncScansResource(self._client)

    @cached_property
    def dom(self) -> AsyncDomResource:
        return AsyncDomResource(self._client)

    @cached_property
    def har(self) -> AsyncHarResource:
        return AsyncHarResource(self._client)

    @cached_property
    def result(self) -> AsyncResultResource:
        return AsyncResultResource(self._client)

    @cached_property
    def screenshot(self) -> AsyncScreenshotResource:
        return AsyncScreenshotResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncURLScannerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncURLScannerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncURLScannerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncURLScannerResourceWithStreamingResponse(self)


class URLScannerResourceWithRawResponse:
    def __init__(self, url_scanner: URLScannerResource) -> None:
        self._url_scanner = url_scanner

    @cached_property
    def responses(self) -> ResponsesResourceWithRawResponse:
        return ResponsesResourceWithRawResponse(self._url_scanner.responses)

    @cached_property
    def scans(self) -> ScansResourceWithRawResponse:
        return ScansResourceWithRawResponse(self._url_scanner.scans)

    @cached_property
    def dom(self) -> DomResourceWithRawResponse:
        return DomResourceWithRawResponse(self._url_scanner.dom)

    @cached_property
    def har(self) -> HarResourceWithRawResponse:
        return HarResourceWithRawResponse(self._url_scanner.har)

    @cached_property
    def result(self) -> ResultResourceWithRawResponse:
        return ResultResourceWithRawResponse(self._url_scanner.result)

    @cached_property
    def screenshot(self) -> ScreenshotResourceWithRawResponse:
        return ScreenshotResourceWithRawResponse(self._url_scanner.screenshot)


class AsyncURLScannerResourceWithRawResponse:
    def __init__(self, url_scanner: AsyncURLScannerResource) -> None:
        self._url_scanner = url_scanner

    @cached_property
    def responses(self) -> AsyncResponsesResourceWithRawResponse:
        return AsyncResponsesResourceWithRawResponse(self._url_scanner.responses)

    @cached_property
    def scans(self) -> AsyncScansResourceWithRawResponse:
        return AsyncScansResourceWithRawResponse(self._url_scanner.scans)

    @cached_property
    def dom(self) -> AsyncDomResourceWithRawResponse:
        return AsyncDomResourceWithRawResponse(self._url_scanner.dom)

    @cached_property
    def har(self) -> AsyncHarResourceWithRawResponse:
        return AsyncHarResourceWithRawResponse(self._url_scanner.har)

    @cached_property
    def result(self) -> AsyncResultResourceWithRawResponse:
        return AsyncResultResourceWithRawResponse(self._url_scanner.result)

    @cached_property
    def screenshot(self) -> AsyncScreenshotResourceWithRawResponse:
        return AsyncScreenshotResourceWithRawResponse(self._url_scanner.screenshot)


class URLScannerResourceWithStreamingResponse:
    def __init__(self, url_scanner: URLScannerResource) -> None:
        self._url_scanner = url_scanner

    @cached_property
    def responses(self) -> ResponsesResourceWithStreamingResponse:
        return ResponsesResourceWithStreamingResponse(self._url_scanner.responses)

    @cached_property
    def scans(self) -> ScansResourceWithStreamingResponse:
        return ScansResourceWithStreamingResponse(self._url_scanner.scans)

    @cached_property
    def dom(self) -> DomResourceWithStreamingResponse:
        return DomResourceWithStreamingResponse(self._url_scanner.dom)

    @cached_property
    def har(self) -> HarResourceWithStreamingResponse:
        return HarResourceWithStreamingResponse(self._url_scanner.har)

    @cached_property
    def result(self) -> ResultResourceWithStreamingResponse:
        return ResultResourceWithStreamingResponse(self._url_scanner.result)

    @cached_property
    def screenshot(self) -> ScreenshotResourceWithStreamingResponse:
        return ScreenshotResourceWithStreamingResponse(self._url_scanner.screenshot)


class AsyncURLScannerResourceWithStreamingResponse:
    def __init__(self, url_scanner: AsyncURLScannerResource) -> None:
        self._url_scanner = url_scanner

    @cached_property
    def responses(self) -> AsyncResponsesResourceWithStreamingResponse:
        return AsyncResponsesResourceWithStreamingResponse(self._url_scanner.responses)

    @cached_property
    def scans(self) -> AsyncScansResourceWithStreamingResponse:
        return AsyncScansResourceWithStreamingResponse(self._url_scanner.scans)

    @cached_property
    def dom(self) -> AsyncDomResourceWithStreamingResponse:
        return AsyncDomResourceWithStreamingResponse(self._url_scanner.dom)

    @cached_property
    def har(self) -> AsyncHarResourceWithStreamingResponse:
        return AsyncHarResourceWithStreamingResponse(self._url_scanner.har)

    @cached_property
    def result(self) -> AsyncResultResourceWithStreamingResponse:
        return AsyncResultResourceWithStreamingResponse(self._url_scanner.result)

    @cached_property
    def screenshot(self) -> AsyncScreenshotResourceWithStreamingResponse:
        return AsyncScreenshotResourceWithStreamingResponse(self._url_scanner.screenshot)
