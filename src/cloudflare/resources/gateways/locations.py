# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.gateways import (
    LocationUpdateResponse,
    LocationDeleteResponse,
    LocationGetResponse,
    LocationZeroTrustGatewayLocationsCreateZeroTrustGatewayLocationResponse,
    LocationZeroTrustGatewayLocationsListZeroTrustGatewayLocationsResponse,
    location_update_params,
    location_zero_trust_gateway_locations_create_zero_trust_gateway_location_params,
)

from typing import Type, Iterable, Optional

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
from ...types.gateways import location_update_params
from ...types.gateways import location_zero_trust_gateway_locations_create_zero_trust_gateway_location_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Locations", "AsyncLocations"]


class Locations(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LocationsWithRawResponse:
        return LocationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LocationsWithStreamingResponse:
        return LocationsWithStreamingResponse(self)

    def update(
        self,
        location_id: object,
        *,
        account_id: object,
        name: str,
        client_default: bool | NotGiven = NOT_GIVEN,
        ecs_support: bool | NotGiven = NOT_GIVEN,
        networks: Iterable[location_update_params.Network] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LocationUpdateResponse:
        """
        Updates a configured Zero Trust Gateway location.

        Args:
          name: The name of the location.

          client_default: True if the location is the default location.

          ecs_support: True if the location needs to resolve EDNS queries.

          networks: A list of network ranges that requests from this location would originate from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/accounts/{account_id}/gateway/locations/{location_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "client_default": client_default,
                    "ecs_support": ecs_support,
                    "networks": networks,
                },
                location_update_params.LocationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LocationUpdateResponse], ResultWrapper[LocationUpdateResponse]),
        )

    def delete(
        self,
        location_id: object,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LocationDeleteResponse:
        """
        Deletes a configured Zero Trust Gateway location.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            LocationDeleteResponse,
            self._delete(
                f"/accounts/{account_id}/gateway/locations/{location_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[LocationDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        location_id: object,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LocationGetResponse:
        """
        Fetches a single Zero Trust Gateway location.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/gateway/locations/{location_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LocationGetResponse], ResultWrapper[LocationGetResponse]),
        )

    def zero_trust_gateway_locations_create_zero_trust_gateway_location(
        self,
        account_id: object,
        *,
        name: str,
        client_default: bool | NotGiven = NOT_GIVEN,
        ecs_support: bool | NotGiven = NOT_GIVEN,
        networks: Iterable[location_zero_trust_gateway_locations_create_zero_trust_gateway_location_params.Network]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LocationZeroTrustGatewayLocationsCreateZeroTrustGatewayLocationResponse:
        """
        Creates a new Zero Trust Gateway location.

        Args:
          name: The name of the location.

          client_default: True if the location is the default location.

          ecs_support: True if the location needs to resolve EDNS queries.

          networks: A list of network ranges that requests from this location would originate from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/accounts/{account_id}/gateway/locations",
            body=maybe_transform(
                {
                    "name": name,
                    "client_default": client_default,
                    "ecs_support": ecs_support,
                    "networks": networks,
                },
                location_zero_trust_gateway_locations_create_zero_trust_gateway_location_params.LocationZeroTrustGatewayLocationsCreateZeroTrustGatewayLocationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[LocationZeroTrustGatewayLocationsCreateZeroTrustGatewayLocationResponse],
                ResultWrapper[LocationZeroTrustGatewayLocationsCreateZeroTrustGatewayLocationResponse],
            ),
        )

    def zero_trust_gateway_locations_list_zero_trust_gateway_locations(
        self,
        account_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LocationZeroTrustGatewayLocationsListZeroTrustGatewayLocationsResponse]:
        """
        Fetches Zero Trust Gateway locations for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/gateway/locations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[LocationZeroTrustGatewayLocationsListZeroTrustGatewayLocationsResponse]],
                ResultWrapper[LocationZeroTrustGatewayLocationsListZeroTrustGatewayLocationsResponse],
            ),
        )


class AsyncLocations(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLocationsWithRawResponse:
        return AsyncLocationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLocationsWithStreamingResponse:
        return AsyncLocationsWithStreamingResponse(self)

    async def update(
        self,
        location_id: object,
        *,
        account_id: object,
        name: str,
        client_default: bool | NotGiven = NOT_GIVEN,
        ecs_support: bool | NotGiven = NOT_GIVEN,
        networks: Iterable[location_update_params.Network] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LocationUpdateResponse:
        """
        Updates a configured Zero Trust Gateway location.

        Args:
          name: The name of the location.

          client_default: True if the location is the default location.

          ecs_support: True if the location needs to resolve EDNS queries.

          networks: A list of network ranges that requests from this location would originate from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/accounts/{account_id}/gateway/locations/{location_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "client_default": client_default,
                    "ecs_support": ecs_support,
                    "networks": networks,
                },
                location_update_params.LocationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LocationUpdateResponse], ResultWrapper[LocationUpdateResponse]),
        )

    async def delete(
        self,
        location_id: object,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LocationDeleteResponse:
        """
        Deletes a configured Zero Trust Gateway location.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            LocationDeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/gateway/locations/{location_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[LocationDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        location_id: object,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LocationGetResponse:
        """
        Fetches a single Zero Trust Gateway location.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/gateway/locations/{location_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LocationGetResponse], ResultWrapper[LocationGetResponse]),
        )

    async def zero_trust_gateway_locations_create_zero_trust_gateway_location(
        self,
        account_id: object,
        *,
        name: str,
        client_default: bool | NotGiven = NOT_GIVEN,
        ecs_support: bool | NotGiven = NOT_GIVEN,
        networks: Iterable[location_zero_trust_gateway_locations_create_zero_trust_gateway_location_params.Network]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LocationZeroTrustGatewayLocationsCreateZeroTrustGatewayLocationResponse:
        """
        Creates a new Zero Trust Gateway location.

        Args:
          name: The name of the location.

          client_default: True if the location is the default location.

          ecs_support: True if the location needs to resolve EDNS queries.

          networks: A list of network ranges that requests from this location would originate from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/accounts/{account_id}/gateway/locations",
            body=maybe_transform(
                {
                    "name": name,
                    "client_default": client_default,
                    "ecs_support": ecs_support,
                    "networks": networks,
                },
                location_zero_trust_gateway_locations_create_zero_trust_gateway_location_params.LocationZeroTrustGatewayLocationsCreateZeroTrustGatewayLocationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[LocationZeroTrustGatewayLocationsCreateZeroTrustGatewayLocationResponse],
                ResultWrapper[LocationZeroTrustGatewayLocationsCreateZeroTrustGatewayLocationResponse],
            ),
        )

    async def zero_trust_gateway_locations_list_zero_trust_gateway_locations(
        self,
        account_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LocationZeroTrustGatewayLocationsListZeroTrustGatewayLocationsResponse]:
        """
        Fetches Zero Trust Gateway locations for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/gateway/locations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[LocationZeroTrustGatewayLocationsListZeroTrustGatewayLocationsResponse]],
                ResultWrapper[LocationZeroTrustGatewayLocationsListZeroTrustGatewayLocationsResponse],
            ),
        )


class LocationsWithRawResponse:
    def __init__(self, locations: Locations) -> None:
        self._locations = locations

        self.update = to_raw_response_wrapper(
            locations.update,
        )
        self.delete = to_raw_response_wrapper(
            locations.delete,
        )
        self.get = to_raw_response_wrapper(
            locations.get,
        )
        self.zero_trust_gateway_locations_create_zero_trust_gateway_location = to_raw_response_wrapper(
            locations.zero_trust_gateway_locations_create_zero_trust_gateway_location,
        )
        self.zero_trust_gateway_locations_list_zero_trust_gateway_locations = to_raw_response_wrapper(
            locations.zero_trust_gateway_locations_list_zero_trust_gateway_locations,
        )


class AsyncLocationsWithRawResponse:
    def __init__(self, locations: AsyncLocations) -> None:
        self._locations = locations

        self.update = async_to_raw_response_wrapper(
            locations.update,
        )
        self.delete = async_to_raw_response_wrapper(
            locations.delete,
        )
        self.get = async_to_raw_response_wrapper(
            locations.get,
        )
        self.zero_trust_gateway_locations_create_zero_trust_gateway_location = async_to_raw_response_wrapper(
            locations.zero_trust_gateway_locations_create_zero_trust_gateway_location,
        )
        self.zero_trust_gateway_locations_list_zero_trust_gateway_locations = async_to_raw_response_wrapper(
            locations.zero_trust_gateway_locations_list_zero_trust_gateway_locations,
        )


class LocationsWithStreamingResponse:
    def __init__(self, locations: Locations) -> None:
        self._locations = locations

        self.update = to_streamed_response_wrapper(
            locations.update,
        )
        self.delete = to_streamed_response_wrapper(
            locations.delete,
        )
        self.get = to_streamed_response_wrapper(
            locations.get,
        )
        self.zero_trust_gateway_locations_create_zero_trust_gateway_location = to_streamed_response_wrapper(
            locations.zero_trust_gateway_locations_create_zero_trust_gateway_location,
        )
        self.zero_trust_gateway_locations_list_zero_trust_gateway_locations = to_streamed_response_wrapper(
            locations.zero_trust_gateway_locations_list_zero_trust_gateway_locations,
        )


class AsyncLocationsWithStreamingResponse:
    def __init__(self, locations: AsyncLocations) -> None:
        self._locations = locations

        self.update = async_to_streamed_response_wrapper(
            locations.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            locations.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            locations.get,
        )
        self.zero_trust_gateway_locations_create_zero_trust_gateway_location = async_to_streamed_response_wrapper(
            locations.zero_trust_gateway_locations_create_zero_trust_gateway_location,
        )
        self.zero_trust_gateway_locations_list_zero_trust_gateway_locations = async_to_streamed_response_wrapper(
            locations.zero_trust_gateway_locations_list_zero_trust_gateway_locations,
        )
