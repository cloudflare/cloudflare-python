# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.api_gateways import DiscoveryAPIShieldEndpointManagementGetAPIDiscoveryResultsForAZoneResponse

from typing import Type

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
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Discoveries", "AsyncDiscoveries"]


class Discoveries(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DiscoveriesWithRawResponse:
        return DiscoveriesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DiscoveriesWithStreamingResponse:
        return DiscoveriesWithStreamingResponse(self)

    def api_shield_endpoint_management_get_api_discovery_results_for_a_zone(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiscoveryAPIShieldEndpointManagementGetAPIDiscoveryResultsForAZoneResponse:
        """
        Retrieve the most up to date view of discovered operations, rendered as OpenAPI
        schemas

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/api_gateway/discovery",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[DiscoveryAPIShieldEndpointManagementGetAPIDiscoveryResultsForAZoneResponse],
                ResultWrapper[DiscoveryAPIShieldEndpointManagementGetAPIDiscoveryResultsForAZoneResponse],
            ),
        )


class AsyncDiscoveries(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDiscoveriesWithRawResponse:
        return AsyncDiscoveriesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDiscoveriesWithStreamingResponse:
        return AsyncDiscoveriesWithStreamingResponse(self)

    async def api_shield_endpoint_management_get_api_discovery_results_for_a_zone(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiscoveryAPIShieldEndpointManagementGetAPIDiscoveryResultsForAZoneResponse:
        """
        Retrieve the most up to date view of discovered operations, rendered as OpenAPI
        schemas

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/api_gateway/discovery",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[DiscoveryAPIShieldEndpointManagementGetAPIDiscoveryResultsForAZoneResponse],
                ResultWrapper[DiscoveryAPIShieldEndpointManagementGetAPIDiscoveryResultsForAZoneResponse],
            ),
        )


class DiscoveriesWithRawResponse:
    def __init__(self, discoveries: Discoveries) -> None:
        self._discoveries = discoveries

        self.api_shield_endpoint_management_get_api_discovery_results_for_a_zone = to_raw_response_wrapper(
            discoveries.api_shield_endpoint_management_get_api_discovery_results_for_a_zone,
        )


class AsyncDiscoveriesWithRawResponse:
    def __init__(self, discoveries: AsyncDiscoveries) -> None:
        self._discoveries = discoveries

        self.api_shield_endpoint_management_get_api_discovery_results_for_a_zone = async_to_raw_response_wrapper(
            discoveries.api_shield_endpoint_management_get_api_discovery_results_for_a_zone,
        )


class DiscoveriesWithStreamingResponse:
    def __init__(self, discoveries: Discoveries) -> None:
        self._discoveries = discoveries

        self.api_shield_endpoint_management_get_api_discovery_results_for_a_zone = to_streamed_response_wrapper(
            discoveries.api_shield_endpoint_management_get_api_discovery_results_for_a_zone,
        )


class AsyncDiscoveriesWithStreamingResponse:
    def __init__(self, discoveries: AsyncDiscoveries) -> None:
        self._discoveries = discoveries

        self.api_shield_endpoint_management_get_api_discovery_results_for_a_zone = async_to_streamed_response_wrapper(
            discoveries.api_shield_endpoint_management_get_api_discovery_results_for_a_zone,
        )
