# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from .asns import (
    ASNs,
    AsyncASNs,
    ASNsWithRawResponse,
    AsyncASNsWithRawResponse,
    ASNsWithStreamingResponse,
    AsyncASNsWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .locations import (
    Locations,
    AsyncLocations,
    LocationsWithRawResponse,
    AsyncLocationsWithRawResponse,
    LocationsWithStreamingResponse,
    AsyncLocationsWithStreamingResponse,
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
from ....types.radar import EntityGetResponse, entity_get_params
from ...._base_client import (
    make_request_options,
)

__all__ = ["Entities", "AsyncEntities"]


class Entities(SyncAPIResource):
    @cached_property
    def asns(self) -> ASNs:
        return ASNs(self._client)

    @cached_property
    def locations(self) -> Locations:
        return Locations(self._client)

    @cached_property
    def with_raw_response(self) -> EntitiesWithRawResponse:
        return EntitiesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntitiesWithStreamingResponse:
        return EntitiesWithStreamingResponse(self)

    def get(
        self,
        *,
        ip: str,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityGetResponse:
        """
        Get IP address information.

        Args:
          ip: IP address.

          format: Format results are returned in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/entities/ip",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ip": ip,
                        "format": format,
                    },
                    entity_get_params.EntityGetParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[EntityGetResponse], ResultWrapper[EntityGetResponse]),
        )


class AsyncEntities(AsyncAPIResource):
    @cached_property
    def asns(self) -> AsyncASNs:
        return AsyncASNs(self._client)

    @cached_property
    def locations(self) -> AsyncLocations:
        return AsyncLocations(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEntitiesWithRawResponse:
        return AsyncEntitiesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntitiesWithStreamingResponse:
        return AsyncEntitiesWithStreamingResponse(self)

    async def get(
        self,
        *,
        ip: str,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityGetResponse:
        """
        Get IP address information.

        Args:
          ip: IP address.

          format: Format results are returned in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/entities/ip",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ip": ip,
                        "format": format,
                    },
                    entity_get_params.EntityGetParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[EntityGetResponse], ResultWrapper[EntityGetResponse]),
        )


class EntitiesWithRawResponse:
    def __init__(self, entities: Entities) -> None:
        self._entities = entities

        self.get = to_raw_response_wrapper(
            entities.get,
        )

    @cached_property
    def asns(self) -> ASNsWithRawResponse:
        return ASNsWithRawResponse(self._entities.asns)

    @cached_property
    def locations(self) -> LocationsWithRawResponse:
        return LocationsWithRawResponse(self._entities.locations)


class AsyncEntitiesWithRawResponse:
    def __init__(self, entities: AsyncEntities) -> None:
        self._entities = entities

        self.get = async_to_raw_response_wrapper(
            entities.get,
        )

    @cached_property
    def asns(self) -> AsyncASNsWithRawResponse:
        return AsyncASNsWithRawResponse(self._entities.asns)

    @cached_property
    def locations(self) -> AsyncLocationsWithRawResponse:
        return AsyncLocationsWithRawResponse(self._entities.locations)


class EntitiesWithStreamingResponse:
    def __init__(self, entities: Entities) -> None:
        self._entities = entities

        self.get = to_streamed_response_wrapper(
            entities.get,
        )

    @cached_property
    def asns(self) -> ASNsWithStreamingResponse:
        return ASNsWithStreamingResponse(self._entities.asns)

    @cached_property
    def locations(self) -> LocationsWithStreamingResponse:
        return LocationsWithStreamingResponse(self._entities.locations)


class AsyncEntitiesWithStreamingResponse:
    def __init__(self, entities: AsyncEntities) -> None:
        self._entities = entities

        self.get = async_to_streamed_response_wrapper(
            entities.get,
        )

    @cached_property
    def asns(self) -> AsyncASNsWithStreamingResponse:
        return AsyncASNsWithStreamingResponse(self._entities.asns)

    @cached_property
    def locations(self) -> AsyncLocationsWithStreamingResponse:
        return AsyncLocationsWithStreamingResponse(self._entities.locations)
