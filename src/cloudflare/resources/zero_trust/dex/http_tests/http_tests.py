# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast
from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from .percentiles import (
    PercentilesResource,
    AsyncPercentilesResource,
    PercentilesResourceWithRawResponse,
    AsyncPercentilesResourceWithRawResponse,
    PercentilesResourceWithStreamingResponse,
    AsyncPercentilesResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import make_request_options
from .....types.zero_trust.dex import http_test_get_params
from .....types.zero_trust.dex.http_details import HTTPDetails

__all__ = ["HTTPTestsResource", "AsyncHTTPTestsResource"]


class HTTPTestsResource(SyncAPIResource):
    @cached_property
    def percentiles(self) -> PercentilesResource:
        return PercentilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> HTTPTestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return HTTPTestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HTTPTestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return HTTPTestsResourceWithStreamingResponse(self)

    def get(
        self,
        test_id: str,
        *,
        account_id: str,
        from_: str,
        interval: Literal["minute", "hour"],
        to: str,
        colo: str | NotGiven = NOT_GIVEN,
        device_id: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HTTPDetails]:
        """
        Get test details and aggregate performance metrics for an http test for a given
        time period between 1 hour and 7 days.

        Args:
          test_id: API Resource UUID tag.

          from_: Start time for aggregate metrics in ISO ms

          interval: Time interval for aggregate time slots.

          to: End time for aggregate metrics in ISO ms

          colo: Optionally filter result stats to a Cloudflare colo. Cannot be used in
              combination with deviceId param.

          device_id: Optionally filter result stats to a specific device(s). Cannot be used in
              combination with colo param.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not test_id:
            raise ValueError(f"Expected a non-empty value for `test_id` but received {test_id!r}")
        return self._get(
            f"/accounts/{account_id}/dex/http-tests/{test_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "interval": interval,
                        "to": to,
                        "colo": colo,
                        "device_id": device_id,
                    },
                    http_test_get_params.HTTPTestGetParams,
                ),
                post_parser=ResultWrapper[Optional[HTTPDetails]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[HTTPDetails]], ResultWrapper[HTTPDetails]),
        )


class AsyncHTTPTestsResource(AsyncAPIResource):
    @cached_property
    def percentiles(self) -> AsyncPercentilesResource:
        return AsyncPercentilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHTTPTestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHTTPTestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHTTPTestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncHTTPTestsResourceWithStreamingResponse(self)

    async def get(
        self,
        test_id: str,
        *,
        account_id: str,
        from_: str,
        interval: Literal["minute", "hour"],
        to: str,
        colo: str | NotGiven = NOT_GIVEN,
        device_id: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HTTPDetails]:
        """
        Get test details and aggregate performance metrics for an http test for a given
        time period between 1 hour and 7 days.

        Args:
          test_id: API Resource UUID tag.

          from_: Start time for aggregate metrics in ISO ms

          interval: Time interval for aggregate time slots.

          to: End time for aggregate metrics in ISO ms

          colo: Optionally filter result stats to a Cloudflare colo. Cannot be used in
              combination with deviceId param.

          device_id: Optionally filter result stats to a specific device(s). Cannot be used in
              combination with colo param.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not test_id:
            raise ValueError(f"Expected a non-empty value for `test_id` but received {test_id!r}")
        return await self._get(
            f"/accounts/{account_id}/dex/http-tests/{test_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "interval": interval,
                        "to": to,
                        "colo": colo,
                        "device_id": device_id,
                    },
                    http_test_get_params.HTTPTestGetParams,
                ),
                post_parser=ResultWrapper[Optional[HTTPDetails]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[HTTPDetails]], ResultWrapper[HTTPDetails]),
        )


class HTTPTestsResourceWithRawResponse:
    def __init__(self, http_tests: HTTPTestsResource) -> None:
        self._http_tests = http_tests

        self.get = to_raw_response_wrapper(
            http_tests.get,
        )

    @cached_property
    def percentiles(self) -> PercentilesResourceWithRawResponse:
        return PercentilesResourceWithRawResponse(self._http_tests.percentiles)


class AsyncHTTPTestsResourceWithRawResponse:
    def __init__(self, http_tests: AsyncHTTPTestsResource) -> None:
        self._http_tests = http_tests

        self.get = async_to_raw_response_wrapper(
            http_tests.get,
        )

    @cached_property
    def percentiles(self) -> AsyncPercentilesResourceWithRawResponse:
        return AsyncPercentilesResourceWithRawResponse(self._http_tests.percentiles)


class HTTPTestsResourceWithStreamingResponse:
    def __init__(self, http_tests: HTTPTestsResource) -> None:
        self._http_tests = http_tests

        self.get = to_streamed_response_wrapper(
            http_tests.get,
        )

    @cached_property
    def percentiles(self) -> PercentilesResourceWithStreamingResponse:
        return PercentilesResourceWithStreamingResponse(self._http_tests.percentiles)


class AsyncHTTPTestsResourceWithStreamingResponse:
    def __init__(self, http_tests: AsyncHTTPTestsResource) -> None:
        self._http_tests = http_tests

        self.get = async_to_streamed_response_wrapper(
            http_tests.get,
        )

    @cached_property
    def percentiles(self) -> AsyncPercentilesResourceWithStreamingResponse:
        return AsyncPercentilesResourceWithStreamingResponse(self._http_tests.percentiles)
