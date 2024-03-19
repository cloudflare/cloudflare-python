# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, cast
from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from .percentiles import (
    Percentiles,
    AsyncPercentiles,
    PercentilesWithRawResponse,
    AsyncPercentilesWithRawResponse,
    PercentilesWithStreamingResponse,
    AsyncPercentilesWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import (
    make_request_options,
)
from .....types.zero_trust.dex import DigitalExperienceMonitoringHTTPDetails, http_test_get_params

__all__ = ["HTTPTests", "AsyncHTTPTests"]


class HTTPTests(SyncAPIResource):
    @cached_property
    def percentiles(self) -> Percentiles:
        return Percentiles(self._client)

    @cached_property
    def with_raw_response(self) -> HTTPTestsWithRawResponse:
        return HTTPTestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HTTPTestsWithStreamingResponse:
        return HTTPTestsWithStreamingResponse(self)

    def get(
        self,
        test_id: str,
        *,
        account_id: str,
        interval: Literal["minute", "hour"],
        time_end: str,
        time_start: str,
        colo: str | NotGiven = NOT_GIVEN,
        device_id: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DigitalExperienceMonitoringHTTPDetails:
        """
        Get test details and aggregate performance metrics for an http test for a given
        time period between 1 hour and 7 days.

        Args:
          test_id: API Resource UUID tag.

          interval: Time interval for aggregate time slots.

          time_end: End time for aggregate metrics in ISO ms

          time_start: Start time for aggregate metrics in ISO ms

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
                        "interval": interval,
                        "time_end": time_end,
                        "time_start": time_start,
                        "colo": colo,
                        "device_id": device_id,
                    },
                    http_test_get_params.HTTPTestGetParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[DigitalExperienceMonitoringHTTPDetails], ResultWrapper[DigitalExperienceMonitoringHTTPDetails]
            ),
        )


class AsyncHTTPTests(AsyncAPIResource):
    @cached_property
    def percentiles(self) -> AsyncPercentiles:
        return AsyncPercentiles(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHTTPTestsWithRawResponse:
        return AsyncHTTPTestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHTTPTestsWithStreamingResponse:
        return AsyncHTTPTestsWithStreamingResponse(self)

    async def get(
        self,
        test_id: str,
        *,
        account_id: str,
        interval: Literal["minute", "hour"],
        time_end: str,
        time_start: str,
        colo: str | NotGiven = NOT_GIVEN,
        device_id: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DigitalExperienceMonitoringHTTPDetails:
        """
        Get test details and aggregate performance metrics for an http test for a given
        time period between 1 hour and 7 days.

        Args:
          test_id: API Resource UUID tag.

          interval: Time interval for aggregate time slots.

          time_end: End time for aggregate metrics in ISO ms

          time_start: Start time for aggregate metrics in ISO ms

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
                        "interval": interval,
                        "time_end": time_end,
                        "time_start": time_start,
                        "colo": colo,
                        "device_id": device_id,
                    },
                    http_test_get_params.HTTPTestGetParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[DigitalExperienceMonitoringHTTPDetails], ResultWrapper[DigitalExperienceMonitoringHTTPDetails]
            ),
        )


class HTTPTestsWithRawResponse:
    def __init__(self, http_tests: HTTPTests) -> None:
        self._http_tests = http_tests

        self.get = to_raw_response_wrapper(
            http_tests.get,
        )

    @cached_property
    def percentiles(self) -> PercentilesWithRawResponse:
        return PercentilesWithRawResponse(self._http_tests.percentiles)


class AsyncHTTPTestsWithRawResponse:
    def __init__(self, http_tests: AsyncHTTPTests) -> None:
        self._http_tests = http_tests

        self.get = async_to_raw_response_wrapper(
            http_tests.get,
        )

    @cached_property
    def percentiles(self) -> AsyncPercentilesWithRawResponse:
        return AsyncPercentilesWithRawResponse(self._http_tests.percentiles)


class HTTPTestsWithStreamingResponse:
    def __init__(self, http_tests: HTTPTests) -> None:
        self._http_tests = http_tests

        self.get = to_streamed_response_wrapper(
            http_tests.get,
        )

    @cached_property
    def percentiles(self) -> PercentilesWithStreamingResponse:
        return PercentilesWithStreamingResponse(self._http_tests.percentiles)


class AsyncHTTPTestsWithStreamingResponse:
    def __init__(self, http_tests: AsyncHTTPTests) -> None:
        self._http_tests = http_tests

        self.get = async_to_streamed_response_wrapper(
            http_tests.get,
        )

    @cached_property
    def percentiles(self) -> AsyncPercentilesWithStreamingResponse:
        return AsyncPercentilesWithStreamingResponse(self._http_tests.percentiles)
