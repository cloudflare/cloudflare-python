# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Iterable, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ....types.zero_trust.gateway import location_create_params, location_update_params
from ....types.zero_trust.gateway.location import Location
from ....types.zero_trust.gateway.location_network_param import LocationNetworkParam
from ....types.zero_trust.gateway.location_delete_response import LocationDeleteResponse

__all__ = ["LocationsResource", "AsyncLocationsResource"]


class LocationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LocationsResourceWithRawResponse:
        return LocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LocationsResourceWithStreamingResponse:
        return LocationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        client_default: bool | NotGiven = NOT_GIVEN,
        ecs_support: bool | NotGiven = NOT_GIVEN,
        networks: Iterable[LocationNetworkParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Location]:
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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/gateway/locations",
            body=maybe_transform(
                {
                    "name": name,
                    "client_default": client_default,
                    "ecs_support": ecs_support,
                    "networks": networks,
                },
                location_create_params.LocationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Location]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Location]], ResultWrapper[Location]),
        )

    def update(
        self,
        location_id: str,
        *,
        account_id: str,
        name: str,
        client_default: bool | NotGiven = NOT_GIVEN,
        ecs_support: bool | NotGiven = NOT_GIVEN,
        networks: Iterable[LocationNetworkParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Location]:
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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not location_id:
            raise ValueError(f"Expected a non-empty value for `location_id` but received {location_id!r}")
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
                post_parser=ResultWrapper[Optional[Location]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Location]], ResultWrapper[Location]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[Location]:
        """
        Fetches Zero Trust Gateway locations for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/gateway/locations",
            page=SyncSinglePage[Location],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Location,
        )

    def delete(
        self,
        location_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LocationDeleteResponse]:
        """
        Deletes a configured Zero Trust Gateway location.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not location_id:
            raise ValueError(f"Expected a non-empty value for `location_id` but received {location_id!r}")
        return cast(
            Optional[LocationDeleteResponse],
            self._delete(
                f"/accounts/{account_id}/gateway/locations/{location_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[LocationDeleteResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[LocationDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        location_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Location]:
        """
        Fetches a single Zero Trust Gateway location.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not location_id:
            raise ValueError(f"Expected a non-empty value for `location_id` but received {location_id!r}")
        return self._get(
            f"/accounts/{account_id}/gateway/locations/{location_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Location]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Location]], ResultWrapper[Location]),
        )


class AsyncLocationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLocationsResourceWithRawResponse:
        return AsyncLocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLocationsResourceWithStreamingResponse:
        return AsyncLocationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        client_default: bool | NotGiven = NOT_GIVEN,
        ecs_support: bool | NotGiven = NOT_GIVEN,
        networks: Iterable[LocationNetworkParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Location]:
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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/gateway/locations",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "client_default": client_default,
                    "ecs_support": ecs_support,
                    "networks": networks,
                },
                location_create_params.LocationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Location]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Location]], ResultWrapper[Location]),
        )

    async def update(
        self,
        location_id: str,
        *,
        account_id: str,
        name: str,
        client_default: bool | NotGiven = NOT_GIVEN,
        ecs_support: bool | NotGiven = NOT_GIVEN,
        networks: Iterable[LocationNetworkParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Location]:
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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not location_id:
            raise ValueError(f"Expected a non-empty value for `location_id` but received {location_id!r}")
        return await self._put(
            f"/accounts/{account_id}/gateway/locations/{location_id}",
            body=await async_maybe_transform(
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
                post_parser=ResultWrapper[Optional[Location]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Location]], ResultWrapper[Location]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Location, AsyncSinglePage[Location]]:
        """
        Fetches Zero Trust Gateway locations for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/gateway/locations",
            page=AsyncSinglePage[Location],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Location,
        )

    async def delete(
        self,
        location_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LocationDeleteResponse]:
        """
        Deletes a configured Zero Trust Gateway location.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not location_id:
            raise ValueError(f"Expected a non-empty value for `location_id` but received {location_id!r}")
        return cast(
            Optional[LocationDeleteResponse],
            await self._delete(
                f"/accounts/{account_id}/gateway/locations/{location_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[LocationDeleteResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[LocationDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        location_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Location]:
        """
        Fetches a single Zero Trust Gateway location.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not location_id:
            raise ValueError(f"Expected a non-empty value for `location_id` but received {location_id!r}")
        return await self._get(
            f"/accounts/{account_id}/gateway/locations/{location_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Location]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Location]], ResultWrapper[Location]),
        )


class LocationsResourceWithRawResponse:
    def __init__(self, locations: LocationsResource) -> None:
        self._locations = locations

        self.create = to_raw_response_wrapper(
            locations.create,
        )
        self.update = to_raw_response_wrapper(
            locations.update,
        )
        self.list = to_raw_response_wrapper(
            locations.list,
        )
        self.delete = to_raw_response_wrapper(
            locations.delete,
        )
        self.get = to_raw_response_wrapper(
            locations.get,
        )


class AsyncLocationsResourceWithRawResponse:
    def __init__(self, locations: AsyncLocationsResource) -> None:
        self._locations = locations

        self.create = async_to_raw_response_wrapper(
            locations.create,
        )
        self.update = async_to_raw_response_wrapper(
            locations.update,
        )
        self.list = async_to_raw_response_wrapper(
            locations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            locations.delete,
        )
        self.get = async_to_raw_response_wrapper(
            locations.get,
        )


class LocationsResourceWithStreamingResponse:
    def __init__(self, locations: LocationsResource) -> None:
        self._locations = locations

        self.create = to_streamed_response_wrapper(
            locations.create,
        )
        self.update = to_streamed_response_wrapper(
            locations.update,
        )
        self.list = to_streamed_response_wrapper(
            locations.list,
        )
        self.delete = to_streamed_response_wrapper(
            locations.delete,
        )
        self.get = to_streamed_response_wrapper(
            locations.get,
        )


class AsyncLocationsResourceWithStreamingResponse:
    def __init__(self, locations: AsyncLocationsResource) -> None:
        self._locations = locations

        self.create = async_to_streamed_response_wrapper(
            locations.create,
        )
        self.update = async_to_streamed_response_wrapper(
            locations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            locations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            locations.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            locations.get,
        )
