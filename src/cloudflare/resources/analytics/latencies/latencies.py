# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .colos import Colos, AsyncColos

from ...._compat import cached_property

from ....types.analytics import LatencyArgoAnalyticsForZoneArgoAnalyticsForAZoneResponse

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ....types.analytics import latency_argo_analytics_for_zone_argo_analytics_for_a_zone_params
from .colos import (
    Colos,
    AsyncColos,
    ColosWithRawResponse,
    AsyncColosWithRawResponse,
    ColosWithStreamingResponse,
    AsyncColosWithStreamingResponse,
)
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Latencies", "AsyncLatencies"]


class Latencies(SyncAPIResource):
    @cached_property
    def colos(self) -> Colos:
        return Colos(self._client)

    @cached_property
    def with_raw_response(self) -> LatenciesWithRawResponse:
        return LatenciesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LatenciesWithStreamingResponse:
        return LatenciesWithStreamingResponse(self)

    def argo_analytics_for_zone_argo_analytics_for_a_zone(
        self,
        zone_id: str,
        *,
        bins: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LatencyArgoAnalyticsForZoneArgoAnalyticsForAZoneResponse:
        """
        Argo Analytics for a zone

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            LatencyArgoAnalyticsForZoneArgoAnalyticsForAZoneResponse,
            self._get(
                f"/zones/{zone_id}/analytics/latency",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {"bins": bins},
                        latency_argo_analytics_for_zone_argo_analytics_for_a_zone_params.LatencyArgoAnalyticsForZoneArgoAnalyticsForAZoneParams,
                    ),
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[LatencyArgoAnalyticsForZoneArgoAnalyticsForAZoneResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncLatencies(AsyncAPIResource):
    @cached_property
    def colos(self) -> AsyncColos:
        return AsyncColos(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLatenciesWithRawResponse:
        return AsyncLatenciesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLatenciesWithStreamingResponse:
        return AsyncLatenciesWithStreamingResponse(self)

    async def argo_analytics_for_zone_argo_analytics_for_a_zone(
        self,
        zone_id: str,
        *,
        bins: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LatencyArgoAnalyticsForZoneArgoAnalyticsForAZoneResponse:
        """
        Argo Analytics for a zone

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            LatencyArgoAnalyticsForZoneArgoAnalyticsForAZoneResponse,
            await self._get(
                f"/zones/{zone_id}/analytics/latency",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {"bins": bins},
                        latency_argo_analytics_for_zone_argo_analytics_for_a_zone_params.LatencyArgoAnalyticsForZoneArgoAnalyticsForAZoneParams,
                    ),
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[LatencyArgoAnalyticsForZoneArgoAnalyticsForAZoneResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class LatenciesWithRawResponse:
    def __init__(self, latencies: Latencies) -> None:
        self._latencies = latencies

        self.argo_analytics_for_zone_argo_analytics_for_a_zone = to_raw_response_wrapper(
            latencies.argo_analytics_for_zone_argo_analytics_for_a_zone,
        )

    @cached_property
    def colos(self) -> ColosWithRawResponse:
        return ColosWithRawResponse(self._latencies.colos)


class AsyncLatenciesWithRawResponse:
    def __init__(self, latencies: AsyncLatencies) -> None:
        self._latencies = latencies

        self.argo_analytics_for_zone_argo_analytics_for_a_zone = async_to_raw_response_wrapper(
            latencies.argo_analytics_for_zone_argo_analytics_for_a_zone,
        )

    @cached_property
    def colos(self) -> AsyncColosWithRawResponse:
        return AsyncColosWithRawResponse(self._latencies.colos)


class LatenciesWithStreamingResponse:
    def __init__(self, latencies: Latencies) -> None:
        self._latencies = latencies

        self.argo_analytics_for_zone_argo_analytics_for_a_zone = to_streamed_response_wrapper(
            latencies.argo_analytics_for_zone_argo_analytics_for_a_zone,
        )

    @cached_property
    def colos(self) -> ColosWithStreamingResponse:
        return ColosWithStreamingResponse(self._latencies.colos)


class AsyncLatenciesWithStreamingResponse:
    def __init__(self, latencies: AsyncLatencies) -> None:
        self._latencies = latencies

        self.argo_analytics_for_zone_argo_analytics_for_a_zone = async_to_streamed_response_wrapper(
            latencies.argo_analytics_for_zone_argo_analytics_for_a_zone,
        )

    @cached_property
    def colos(self) -> AsyncColosWithStreamingResponse:
        return AsyncColosWithStreamingResponse(self._latencies.colos)
