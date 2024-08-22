# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .asns import ASNsResource, AsyncASNsResource

from ...._compat import cached_property

from .locations import LocationsResource, AsyncLocationsResource

from ....types.radar.entity_get_response import EntityGetResponse

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options

from typing import Type

from typing_extensions import Literal

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.radar import entity_get_params
from .asns import ASNsResource, AsyncASNsResource, ASNsResourceWithRawResponse, AsyncASNsResourceWithRawResponse, ASNsResourceWithStreamingResponse, AsyncASNsResourceWithStreamingResponse
from .locations import LocationsResource, AsyncLocationsResource, LocationsResourceWithRawResponse, AsyncLocationsResourceWithRawResponse, LocationsResourceWithStreamingResponse, AsyncLocationsResourceWithStreamingResponse
from typing import cast
from typing import cast

__all__ = ["EntitiesResource", "AsyncEntitiesResource"]

class EntitiesResource(SyncAPIResource):
    @cached_property
    def asns(self) -> ASNsResource:
        return ASNsResource(self._client)

    @cached_property
    def locations(self) -> LocationsResource:
        return LocationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EntitiesResourceWithRawResponse:
        return EntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntitiesResourceWithStreamingResponse:
        return EntitiesResourceWithStreamingResponse(self)

    def get(self,
    *,
    ip: str,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> EntityGetResponse:
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
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "ip": ip,
                "format": format,
            }, entity_get_params.EntityGetParams), post_parser=ResultWrapper[EntityGetResponse]._unwrapper),
            cast_to=cast(Type[EntityGetResponse], ResultWrapper[EntityGetResponse]),
        )

class AsyncEntitiesResource(AsyncAPIResource):
    @cached_property
    def asns(self) -> AsyncASNsResource:
        return AsyncASNsResource(self._client)

    @cached_property
    def locations(self) -> AsyncLocationsResource:
        return AsyncLocationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEntitiesResourceWithRawResponse:
        return AsyncEntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntitiesResourceWithStreamingResponse:
        return AsyncEntitiesResourceWithStreamingResponse(self)

    async def get(self,
    *,
    ip: str,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> EntityGetResponse:
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
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "ip": ip,
                "format": format,
            }, entity_get_params.EntityGetParams), post_parser=ResultWrapper[EntityGetResponse]._unwrapper),
            cast_to=cast(Type[EntityGetResponse], ResultWrapper[EntityGetResponse]),
        )

class EntitiesResourceWithRawResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

        self.get = to_raw_response_wrapper(
            entities.get,
        )

    @cached_property
    def asns(self) -> ASNsResourceWithRawResponse:
        return ASNsResourceWithRawResponse(self._entities.asns)

    @cached_property
    def locations(self) -> LocationsResourceWithRawResponse:
        return LocationsResourceWithRawResponse(self._entities.locations)

class AsyncEntitiesResourceWithRawResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

        self.get = async_to_raw_response_wrapper(
            entities.get,
        )

    @cached_property
    def asns(self) -> AsyncASNsResourceWithRawResponse:
        return AsyncASNsResourceWithRawResponse(self._entities.asns)

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithRawResponse:
        return AsyncLocationsResourceWithRawResponse(self._entities.locations)

class EntitiesResourceWithStreamingResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

        self.get = to_streamed_response_wrapper(
            entities.get,
        )

    @cached_property
    def asns(self) -> ASNsResourceWithStreamingResponse:
        return ASNsResourceWithStreamingResponse(self._entities.asns)

    @cached_property
    def locations(self) -> LocationsResourceWithStreamingResponse:
        return LocationsResourceWithStreamingResponse(self._entities.locations)

class AsyncEntitiesResourceWithStreamingResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

        self.get = async_to_streamed_response_wrapper(
            entities.get,
        )

    @cached_property
    def asns(self) -> AsyncASNsResourceWithStreamingResponse:
        return AsyncASNsResourceWithStreamingResponse(self._entities.asns)

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithStreamingResponse:
        return AsyncLocationsResourceWithStreamingResponse(self._entities.locations)