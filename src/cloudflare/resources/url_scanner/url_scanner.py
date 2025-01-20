# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .scans import (
    ScansResource,
    AsyncScansResource,
    ScansResourceWithRawResponse,
    AsyncScansResourceWithRawResponse,
    ScansResourceWithStreamingResponse,
    AsyncScansResourceWithStreamingResponse,
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
    def with_raw_response(self) -> URLScannerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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
    def with_raw_response(self) -> AsyncURLScannerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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


class AsyncURLScannerResourceWithRawResponse:
    def __init__(self, url_scanner: AsyncURLScannerResource) -> None:
        self._url_scanner = url_scanner

    @cached_property
    def responses(self) -> AsyncResponsesResourceWithRawResponse:
        return AsyncResponsesResourceWithRawResponse(self._url_scanner.responses)

    @cached_property
    def scans(self) -> AsyncScansResourceWithRawResponse:
        return AsyncScansResourceWithRawResponse(self._url_scanner.scans)


class URLScannerResourceWithStreamingResponse:
    def __init__(self, url_scanner: URLScannerResource) -> None:
        self._url_scanner = url_scanner

    @cached_property
    def responses(self) -> ResponsesResourceWithStreamingResponse:
        return ResponsesResourceWithStreamingResponse(self._url_scanner.responses)

    @cached_property
    def scans(self) -> ScansResourceWithStreamingResponse:
        return ScansResourceWithStreamingResponse(self._url_scanner.scans)


class AsyncURLScannerResourceWithStreamingResponse:
    def __init__(self, url_scanner: AsyncURLScannerResource) -> None:
        self._url_scanner = url_scanner

    @cached_property
    def responses(self) -> AsyncResponsesResourceWithStreamingResponse:
        return AsyncResponsesResourceWithStreamingResponse(self._url_scanner.responses)

    @cached_property
    def scans(self) -> AsyncScansResourceWithStreamingResponse:
        return AsyncScansResourceWithStreamingResponse(self._url_scanner.scans)
