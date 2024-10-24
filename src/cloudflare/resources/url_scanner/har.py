# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.url_scanner.har_get_response import HARGetResponse

__all__ = ["HARResource", "AsyncHARResource"]


class HARResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HARResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return HARResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HARResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return HARResourceWithStreamingResponse(self)

    def get(
        self,
        scan_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HARGetResponse:
        """Get a URL scan's HAR file.

        See HAR spec at
        http://www.softwareishard.com/blog/har-12-spec/.

        Args:
          account_id: Account Id.

          scan_id: Scan uuid.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        return self._get(
            f"/accounts/{account_id}/urlscanner/v2/har/{scan_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HARGetResponse,
        )


class AsyncHARResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHARResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHARResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHARResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncHARResourceWithStreamingResponse(self)

    async def get(
        self,
        scan_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HARGetResponse:
        """Get a URL scan's HAR file.

        See HAR spec at
        http://www.softwareishard.com/blog/har-12-spec/.

        Args:
          account_id: Account Id.

          scan_id: Scan uuid.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        return await self._get(
            f"/accounts/{account_id}/urlscanner/v2/har/{scan_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HARGetResponse,
        )


class HARResourceWithRawResponse:
    def __init__(self, har: HARResource) -> None:
        self._har = har

        self.get = to_raw_response_wrapper(
            har.get,
        )


class AsyncHARResourceWithRawResponse:
    def __init__(self, har: AsyncHARResource) -> None:
        self._har = har

        self.get = async_to_raw_response_wrapper(
            har.get,
        )


class HARResourceWithStreamingResponse:
    def __init__(self, har: HARResource) -> None:
        self._har = har

        self.get = to_streamed_response_wrapper(
            har.get,
        )


class AsyncHARResourceWithStreamingResponse:
    def __init__(self, har: AsyncHARResource) -> None:
        self._har = har

        self.get = async_to_streamed_response_wrapper(
            har.get,
        )
