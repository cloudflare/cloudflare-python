# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from .dom import (
    DOMResource,
    AsyncDOMResource,
    DOMResourceWithRawResponse,
    AsyncDOMResourceWithRawResponse,
    DOMResourceWithStreamingResponse,
    AsyncDOMResourceWithStreamingResponse,
)
from .har import (
    HARResource,
    AsyncHARResource,
    HARResourceWithRawResponse,
    AsyncHARResourceWithRawResponse,
    HARResourceWithStreamingResponse,
    AsyncHARResourceWithStreamingResponse,
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
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
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
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.url_scanner import url_scanner_bulk_params
from ...types.url_scanner.url_scanner_bulk_response import URLScannerBulkResponse

__all__ = ["URLScannerResource", "AsyncURLScannerResource"]


class URLScannerResource(SyncAPIResource):
    @cached_property
    def responses(self) -> ResponsesResource:
        return ResponsesResource(self._client)

    @cached_property
    def scans(self) -> ScansResource:
        return ScansResource(self._client)

    @cached_property
    def dom(self) -> DOMResource:
        return DOMResource(self._client)

    @cached_property
    def har(self) -> HARResource:
        return HARResource(self._client)

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

    def bulk(
        self,
        account_id: str,
        *,
        body: Iterable[url_scanner_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLScannerBulkResponse:
        """Submit URLs to scan.

        Check limits at
        https://developers.cloudflare.com/security-center/investigate/scan-limits/ and
        take into account scans submitted in bulk have lower priority and may take
        longer to finish.

        Args:
          account_id: Account Id.

          body: List of urls to scan (up to a 100).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/urlscanner/v2/bulk",
            body=maybe_transform(body, Iterable[url_scanner_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLScannerBulkResponse,
        )


class AsyncURLScannerResource(AsyncAPIResource):
    @cached_property
    def responses(self) -> AsyncResponsesResource:
        return AsyncResponsesResource(self._client)

    @cached_property
    def scans(self) -> AsyncScansResource:
        return AsyncScansResource(self._client)

    @cached_property
    def dom(self) -> AsyncDOMResource:
        return AsyncDOMResource(self._client)

    @cached_property
    def har(self) -> AsyncHARResource:
        return AsyncHARResource(self._client)

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

    async def bulk(
        self,
        account_id: str,
        *,
        body: Iterable[url_scanner_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLScannerBulkResponse:
        """Submit URLs to scan.

        Check limits at
        https://developers.cloudflare.com/security-center/investigate/scan-limits/ and
        take into account scans submitted in bulk have lower priority and may take
        longer to finish.

        Args:
          account_id: Account Id.

          body: List of urls to scan (up to a 100).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/urlscanner/v2/bulk",
            body=await async_maybe_transform(body, Iterable[url_scanner_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLScannerBulkResponse,
        )


class URLScannerResourceWithRawResponse:
    def __init__(self, url_scanner: URLScannerResource) -> None:
        self._url_scanner = url_scanner

        self.bulk = to_raw_response_wrapper(
            url_scanner.bulk,
        )

    @cached_property
    def responses(self) -> ResponsesResourceWithRawResponse:
        return ResponsesResourceWithRawResponse(self._url_scanner.responses)

    @cached_property
    def scans(self) -> ScansResourceWithRawResponse:
        return ScansResourceWithRawResponse(self._url_scanner.scans)

    @cached_property
    def dom(self) -> DOMResourceWithRawResponse:
        return DOMResourceWithRawResponse(self._url_scanner.dom)

    @cached_property
    def har(self) -> HARResourceWithRawResponse:
        return HARResourceWithRawResponse(self._url_scanner.har)

    @cached_property
    def result(self) -> ResultResourceWithRawResponse:
        return ResultResourceWithRawResponse(self._url_scanner.result)

    @cached_property
    def screenshot(self) -> ScreenshotResourceWithRawResponse:
        return ScreenshotResourceWithRawResponse(self._url_scanner.screenshot)


class AsyncURLScannerResourceWithRawResponse:
    def __init__(self, url_scanner: AsyncURLScannerResource) -> None:
        self._url_scanner = url_scanner

        self.bulk = async_to_raw_response_wrapper(
            url_scanner.bulk,
        )

    @cached_property
    def responses(self) -> AsyncResponsesResourceWithRawResponse:
        return AsyncResponsesResourceWithRawResponse(self._url_scanner.responses)

    @cached_property
    def scans(self) -> AsyncScansResourceWithRawResponse:
        return AsyncScansResourceWithRawResponse(self._url_scanner.scans)

    @cached_property
    def dom(self) -> AsyncDOMResourceWithRawResponse:
        return AsyncDOMResourceWithRawResponse(self._url_scanner.dom)

    @cached_property
    def har(self) -> AsyncHARResourceWithRawResponse:
        return AsyncHARResourceWithRawResponse(self._url_scanner.har)

    @cached_property
    def result(self) -> AsyncResultResourceWithRawResponse:
        return AsyncResultResourceWithRawResponse(self._url_scanner.result)

    @cached_property
    def screenshot(self) -> AsyncScreenshotResourceWithRawResponse:
        return AsyncScreenshotResourceWithRawResponse(self._url_scanner.screenshot)


class URLScannerResourceWithStreamingResponse:
    def __init__(self, url_scanner: URLScannerResource) -> None:
        self._url_scanner = url_scanner

        self.bulk = to_streamed_response_wrapper(
            url_scanner.bulk,
        )

    @cached_property
    def responses(self) -> ResponsesResourceWithStreamingResponse:
        return ResponsesResourceWithStreamingResponse(self._url_scanner.responses)

    @cached_property
    def scans(self) -> ScansResourceWithStreamingResponse:
        return ScansResourceWithStreamingResponse(self._url_scanner.scans)

    @cached_property
    def dom(self) -> DOMResourceWithStreamingResponse:
        return DOMResourceWithStreamingResponse(self._url_scanner.dom)

    @cached_property
    def har(self) -> HARResourceWithStreamingResponse:
        return HARResourceWithStreamingResponse(self._url_scanner.har)

    @cached_property
    def result(self) -> ResultResourceWithStreamingResponse:
        return ResultResourceWithStreamingResponse(self._url_scanner.result)

    @cached_property
    def screenshot(self) -> ScreenshotResourceWithStreamingResponse:
        return ScreenshotResourceWithStreamingResponse(self._url_scanner.screenshot)


class AsyncURLScannerResourceWithStreamingResponse:
    def __init__(self, url_scanner: AsyncURLScannerResource) -> None:
        self._url_scanner = url_scanner

        self.bulk = async_to_streamed_response_wrapper(
            url_scanner.bulk,
        )

    @cached_property
    def responses(self) -> AsyncResponsesResourceWithStreamingResponse:
        return AsyncResponsesResourceWithStreamingResponse(self._url_scanner.responses)

    @cached_property
    def scans(self) -> AsyncScansResourceWithStreamingResponse:
        return AsyncScansResourceWithStreamingResponse(self._url_scanner.scans)

    @cached_property
    def dom(self) -> AsyncDOMResourceWithStreamingResponse:
        return AsyncDOMResourceWithStreamingResponse(self._url_scanner.dom)

    @cached_property
    def har(self) -> AsyncHARResourceWithStreamingResponse:
        return AsyncHARResourceWithStreamingResponse(self._url_scanner.har)

    @cached_property
    def result(self) -> AsyncResultResourceWithStreamingResponse:
        return AsyncResultResourceWithStreamingResponse(self._url_scanner.result)

    @cached_property
    def screenshot(self) -> AsyncScreenshotResourceWithStreamingResponse:
        return AsyncScreenshotResourceWithStreamingResponse(self._url_scanner.screenshot)
