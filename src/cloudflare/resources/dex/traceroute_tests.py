# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.dex import TracerouteTestGetResponse, TracerouteTestNetworkPathResponse, TracerouteTestPercentilesResponse

from typing import Type, List

from typing_extensions import Literal

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.dex import traceroute_test_get_params
from ...types.dex import traceroute_test_network_path_params
from ...types.dex import traceroute_test_percentiles_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["TracerouteTests", "AsyncTracerouteTests"]


class TracerouteTests(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TracerouteTestsWithRawResponse:
        return TracerouteTestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TracerouteTestsWithStreamingResponse:
        return TracerouteTestsWithStreamingResponse(self)

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
    ) -> TracerouteTestGetResponse:
        """
        Get test details and aggregate performance metrics for an traceroute test for a
        given time period between 1 hour and 7 days.

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
            f"/accounts/{account_id}/dex/traceroute-tests/{test_id}",
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
                    traceroute_test_get_params.TracerouteTestGetParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TracerouteTestGetResponse], ResultWrapper[TracerouteTestGetResponse]),
        )

    def network_path(
        self,
        test_id: str,
        *,
        account_id: str,
        device_id: str,
        interval: Literal["minute", "hour"],
        time_end: str,
        time_start: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TracerouteTestNetworkPathResponse:
        """
        Get a breakdown of metrics by hop for individual traceroute test runs

        Args:
          test_id: API Resource UUID tag.

          device_id: Device to filter tracroute result runs to

          interval: Time interval for aggregate time slots.

          time_end: End time for aggregate metrics in ISO ms

          time_start: Start time for aggregate metrics in ISO ms

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
            f"/accounts/{account_id}/dex/traceroute-tests/{test_id}/network-path",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "device_id": device_id,
                        "interval": interval,
                        "time_end": time_end,
                        "time_start": time_start,
                    },
                    traceroute_test_network_path_params.TracerouteTestNetworkPathParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TracerouteTestNetworkPathResponse], ResultWrapper[TracerouteTestNetworkPathResponse]),
        )

    def percentiles(
        self,
        test_id: str,
        *,
        account_id: str,
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
    ) -> TracerouteTestPercentilesResponse:
        """
        Get percentiles for a traceroute test for a given time period between 1 hour and
        7 days.

        Args:
          test_id: API Resource UUID tag.

          time_end: End time for aggregate metrics in ISO format

          time_start: Start time for aggregate metrics in ISO format

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
            f"/accounts/{account_id}/dex/traceroute-tests/{test_id}/percentiles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "time_end": time_end,
                        "time_start": time_start,
                        "colo": colo,
                        "device_id": device_id,
                    },
                    traceroute_test_percentiles_params.TracerouteTestPercentilesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TracerouteTestPercentilesResponse], ResultWrapper[TracerouteTestPercentilesResponse]),
        )


class AsyncTracerouteTests(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTracerouteTestsWithRawResponse:
        return AsyncTracerouteTestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTracerouteTestsWithStreamingResponse:
        return AsyncTracerouteTestsWithStreamingResponse(self)

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
    ) -> TracerouteTestGetResponse:
        """
        Get test details and aggregate performance metrics for an traceroute test for a
        given time period between 1 hour and 7 days.

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
            f"/accounts/{account_id}/dex/traceroute-tests/{test_id}",
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
                    traceroute_test_get_params.TracerouteTestGetParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TracerouteTestGetResponse], ResultWrapper[TracerouteTestGetResponse]),
        )

    async def network_path(
        self,
        test_id: str,
        *,
        account_id: str,
        device_id: str,
        interval: Literal["minute", "hour"],
        time_end: str,
        time_start: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TracerouteTestNetworkPathResponse:
        """
        Get a breakdown of metrics by hop for individual traceroute test runs

        Args:
          test_id: API Resource UUID tag.

          device_id: Device to filter tracroute result runs to

          interval: Time interval for aggregate time slots.

          time_end: End time for aggregate metrics in ISO ms

          time_start: Start time for aggregate metrics in ISO ms

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
            f"/accounts/{account_id}/dex/traceroute-tests/{test_id}/network-path",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "device_id": device_id,
                        "interval": interval,
                        "time_end": time_end,
                        "time_start": time_start,
                    },
                    traceroute_test_network_path_params.TracerouteTestNetworkPathParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TracerouteTestNetworkPathResponse], ResultWrapper[TracerouteTestNetworkPathResponse]),
        )

    async def percentiles(
        self,
        test_id: str,
        *,
        account_id: str,
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
    ) -> TracerouteTestPercentilesResponse:
        """
        Get percentiles for a traceroute test for a given time period between 1 hour and
        7 days.

        Args:
          test_id: API Resource UUID tag.

          time_end: End time for aggregate metrics in ISO format

          time_start: Start time for aggregate metrics in ISO format

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
            f"/accounts/{account_id}/dex/traceroute-tests/{test_id}/percentiles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "time_end": time_end,
                        "time_start": time_start,
                        "colo": colo,
                        "device_id": device_id,
                    },
                    traceroute_test_percentiles_params.TracerouteTestPercentilesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TracerouteTestPercentilesResponse], ResultWrapper[TracerouteTestPercentilesResponse]),
        )


class TracerouteTestsWithRawResponse:
    def __init__(self, traceroute_tests: TracerouteTests) -> None:
        self._traceroute_tests = traceroute_tests

        self.get = to_raw_response_wrapper(
            traceroute_tests.get,
        )
        self.network_path = to_raw_response_wrapper(
            traceroute_tests.network_path,
        )
        self.percentiles = to_raw_response_wrapper(
            traceroute_tests.percentiles,
        )


class AsyncTracerouteTestsWithRawResponse:
    def __init__(self, traceroute_tests: AsyncTracerouteTests) -> None:
        self._traceroute_tests = traceroute_tests

        self.get = async_to_raw_response_wrapper(
            traceroute_tests.get,
        )
        self.network_path = async_to_raw_response_wrapper(
            traceroute_tests.network_path,
        )
        self.percentiles = async_to_raw_response_wrapper(
            traceroute_tests.percentiles,
        )


class TracerouteTestsWithStreamingResponse:
    def __init__(self, traceroute_tests: TracerouteTests) -> None:
        self._traceroute_tests = traceroute_tests

        self.get = to_streamed_response_wrapper(
            traceroute_tests.get,
        )
        self.network_path = to_streamed_response_wrapper(
            traceroute_tests.network_path,
        )
        self.percentiles = to_streamed_response_wrapper(
            traceroute_tests.percentiles,
        )


class AsyncTracerouteTestsWithStreamingResponse:
    def __init__(self, traceroute_tests: AsyncTracerouteTests) -> None:
        self._traceroute_tests = traceroute_tests

        self.get = async_to_streamed_response_wrapper(
            traceroute_tests.get,
        )
        self.network_path = async_to_streamed_response_wrapper(
            traceroute_tests.network_path,
        )
        self.percentiles = async_to_streamed_response_wrapper(
            traceroute_tests.percentiles,
        )
