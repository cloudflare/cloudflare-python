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
from ...types.url_scanner.result_get_response import ResultGetResponse

__all__ = ["ResultResource", "AsyncResultResource"]


class ResultResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResultResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ResultResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResultResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ResultResourceWithStreamingResponse(self)

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
    ) -> ResultGetResponse:
        """
        Get URL scan by uuid

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
            f"/accounts/{account_id}/urlscanner/v2/result/{scan_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResultGetResponse,
        )


class AsyncResultResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResultResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResultResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResultResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncResultResourceWithStreamingResponse(self)

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
    ) -> ResultGetResponse:
        """
        Get URL scan by uuid

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
            f"/accounts/{account_id}/urlscanner/v2/result/{scan_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResultGetResponse,
        )


class ResultResourceWithRawResponse:
    def __init__(self, result: ResultResource) -> None:
        self._result = result

        self.get = to_raw_response_wrapper(
            result.get,
        )


class AsyncResultResourceWithRawResponse:
    def __init__(self, result: AsyncResultResource) -> None:
        self._result = result

        self.get = async_to_raw_response_wrapper(
            result.get,
        )


class ResultResourceWithStreamingResponse:
    def __init__(self, result: ResultResource) -> None:
        self._result = result

        self.get = to_streamed_response_wrapper(
            result.get,
        )


class AsyncResultResourceWithStreamingResponse:
    def __init__(self, result: AsyncResultResource) -> None:
        self._result = result

        self.get = async_to_streamed_response_wrapper(
            result.get,
        )
