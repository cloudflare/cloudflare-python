# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.zero_trust.dex.traceroute import Traceroute

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type, List

from ...._base_client import make_request_options

from typing_extensions import Literal

from ....types.zero_trust.network_path_response import NetworkPathResponse

from ....types.zero_trust.dex.traceroute_test_percentiles_response import TracerouteTestPercentilesResponse

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.zero_trust.dex import traceroute_test_get_params
from ....types.zero_trust.dex import traceroute_test_network_path_params
from ....types.zero_trust.dex import traceroute_test_percentiles_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["TracerouteTestsResource", "AsyncTracerouteTestsResource"]

class TracerouteTestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TracerouteTestsResourceWithRawResponse:
        return TracerouteTestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TracerouteTestsResourceWithStreamingResponse:
        return TracerouteTestsResourceWithStreamingResponse(self)

    def get(self,
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
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[Traceroute]:
        """
        Get test details and aggregate performance metrics for an traceroute test for a
        given time period between 1 hour and 7 days.

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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not test_id:
          raise ValueError(
            f'Expected a non-empty value for `test_id` but received {test_id!r}'
          )
        return self._get(
            f"/accounts/{account_id}/dex/traceroute-tests/{test_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "from_": from_,
                "interval": interval,
                "to": to,
                "colo": colo,
                "device_id": device_id,
            }, traceroute_test_get_params.TracerouteTestGetParams), post_parser=ResultWrapper[Optional[Traceroute]]._unwrapper),
            cast_to=cast(Type[Optional[Traceroute]], ResultWrapper[Traceroute]),
        )

    def network_path(self,
    test_id: str,
    *,
    account_id: str,
    device_id: str,
    from_: str,
    interval: Literal["minute", "hour"],
    to: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[NetworkPathResponse]:
        """
        Get a breakdown of metrics by hop for individual traceroute test runs

        Args:
          test_id: API Resource UUID tag.

          device_id: Device to filter tracroute result runs to

          from_: Start time for aggregate metrics in ISO ms

          interval: Time interval for aggregate time slots.

          to: End time for aggregate metrics in ISO ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not test_id:
          raise ValueError(
            f'Expected a non-empty value for `test_id` but received {test_id!r}'
          )
        return self._get(
            f"/accounts/{account_id}/dex/traceroute-tests/{test_id}/network-path",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "device_id": device_id,
                "from_": from_,
                "interval": interval,
                "to": to,
            }, traceroute_test_network_path_params.TracerouteTestNetworkPathParams), post_parser=ResultWrapper[Optional[NetworkPathResponse]]._unwrapper),
            cast_to=cast(Type[Optional[NetworkPathResponse]], ResultWrapper[NetworkPathResponse]),
        )

    def percentiles(self,
    test_id: str,
    *,
    account_id: str,
    from_: str,
    to: str,
    colo: str | NotGiven = NOT_GIVEN,
    device_id: List[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[TracerouteTestPercentilesResponse]:
        """
        Get percentiles for a traceroute test for a given time period between 1 hour and
        7 days.

        Args:
          test_id: API Resource UUID tag.

          from_: Start time for aggregate metrics in ISO format

          to: End time for aggregate metrics in ISO format

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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not test_id:
          raise ValueError(
            f'Expected a non-empty value for `test_id` but received {test_id!r}'
          )
        return self._get(
            f"/accounts/{account_id}/dex/traceroute-tests/{test_id}/percentiles",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "from_": from_,
                "to": to,
                "colo": colo,
                "device_id": device_id,
            }, traceroute_test_percentiles_params.TracerouteTestPercentilesParams), post_parser=ResultWrapper[Optional[TracerouteTestPercentilesResponse]]._unwrapper),
            cast_to=cast(Type[Optional[TracerouteTestPercentilesResponse]], ResultWrapper[TracerouteTestPercentilesResponse]),
        )

class AsyncTracerouteTestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTracerouteTestsResourceWithRawResponse:
        return AsyncTracerouteTestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTracerouteTestsResourceWithStreamingResponse:
        return AsyncTracerouteTestsResourceWithStreamingResponse(self)

    async def get(self,
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
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[Traceroute]:
        """
        Get test details and aggregate performance metrics for an traceroute test for a
        given time period between 1 hour and 7 days.

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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not test_id:
          raise ValueError(
            f'Expected a non-empty value for `test_id` but received {test_id!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/dex/traceroute-tests/{test_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "from_": from_,
                "interval": interval,
                "to": to,
                "colo": colo,
                "device_id": device_id,
            }, traceroute_test_get_params.TracerouteTestGetParams), post_parser=ResultWrapper[Optional[Traceroute]]._unwrapper),
            cast_to=cast(Type[Optional[Traceroute]], ResultWrapper[Traceroute]),
        )

    async def network_path(self,
    test_id: str,
    *,
    account_id: str,
    device_id: str,
    from_: str,
    interval: Literal["minute", "hour"],
    to: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[NetworkPathResponse]:
        """
        Get a breakdown of metrics by hop for individual traceroute test runs

        Args:
          test_id: API Resource UUID tag.

          device_id: Device to filter tracroute result runs to

          from_: Start time for aggregate metrics in ISO ms

          interval: Time interval for aggregate time slots.

          to: End time for aggregate metrics in ISO ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not test_id:
          raise ValueError(
            f'Expected a non-empty value for `test_id` but received {test_id!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/dex/traceroute-tests/{test_id}/network-path",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "device_id": device_id,
                "from_": from_,
                "interval": interval,
                "to": to,
            }, traceroute_test_network_path_params.TracerouteTestNetworkPathParams), post_parser=ResultWrapper[Optional[NetworkPathResponse]]._unwrapper),
            cast_to=cast(Type[Optional[NetworkPathResponse]], ResultWrapper[NetworkPathResponse]),
        )

    async def percentiles(self,
    test_id: str,
    *,
    account_id: str,
    from_: str,
    to: str,
    colo: str | NotGiven = NOT_GIVEN,
    device_id: List[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[TracerouteTestPercentilesResponse]:
        """
        Get percentiles for a traceroute test for a given time period between 1 hour and
        7 days.

        Args:
          test_id: API Resource UUID tag.

          from_: Start time for aggregate metrics in ISO format

          to: End time for aggregate metrics in ISO format

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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not test_id:
          raise ValueError(
            f'Expected a non-empty value for `test_id` but received {test_id!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/dex/traceroute-tests/{test_id}/percentiles",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "from_": from_,
                "to": to,
                "colo": colo,
                "device_id": device_id,
            }, traceroute_test_percentiles_params.TracerouteTestPercentilesParams), post_parser=ResultWrapper[Optional[TracerouteTestPercentilesResponse]]._unwrapper),
            cast_to=cast(Type[Optional[TracerouteTestPercentilesResponse]], ResultWrapper[TracerouteTestPercentilesResponse]),
        )

class TracerouteTestsResourceWithRawResponse:
    def __init__(self, traceroute_tests: TracerouteTestsResource) -> None:
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

class AsyncTracerouteTestsResourceWithRawResponse:
    def __init__(self, traceroute_tests: AsyncTracerouteTestsResource) -> None:
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

class TracerouteTestsResourceWithStreamingResponse:
    def __init__(self, traceroute_tests: TracerouteTestsResource) -> None:
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

class AsyncTracerouteTestsResourceWithStreamingResponse:
    def __init__(self, traceroute_tests: AsyncTracerouteTestsResource) -> None:
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