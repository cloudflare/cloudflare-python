# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .asns import Asns, AsyncAsns

from ...._compat import cached_property

from ....types.radar import EntityIPsResponse

from typing import Type

from typing_extensions import Literal

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
from ....types.radar import entity_ips_params
from .asns import (
    Asns,
    AsyncAsns,
    AsnsWithRawResponse,
    AsyncAsnsWithRawResponse,
    AsnsWithStreamingResponse,
    AsyncAsnsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Entities", "AsyncEntities"]


class Entities(SyncAPIResource):
    @cached_property
    def asns(self) -> Asns:
        return Asns(self._client)

    @cached_property
    def with_raw_response(self) -> EntitiesWithRawResponse:
        return EntitiesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntitiesWithStreamingResponse:
        return EntitiesWithStreamingResponse(self)

    def ips(
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
    ) -> EntityIPsResponse:
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
                    entity_ips_params.EntityIPsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[EntityIPsResponse], ResultWrapper[EntityIPsResponse]),
        )


class AsyncEntities(AsyncAPIResource):
    @cached_property
    def asns(self) -> AsyncAsns:
        return AsyncAsns(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEntitiesWithRawResponse:
        return AsyncEntitiesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntitiesWithStreamingResponse:
        return AsyncEntitiesWithStreamingResponse(self)

    async def ips(
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
    ) -> EntityIPsResponse:
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
                query=maybe_transform(
                    {
                        "ip": ip,
                        "format": format,
                    },
                    entity_ips_params.EntityIPsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[EntityIPsResponse], ResultWrapper[EntityIPsResponse]),
        )


class EntitiesWithRawResponse:
    def __init__(self, entities: Entities) -> None:
        self._entities = entities

        self.ips = to_raw_response_wrapper(
            entities.ips,
        )

    @cached_property
    def asns(self) -> AsnsWithRawResponse:
        return AsnsWithRawResponse(self._entities.asns)


class AsyncEntitiesWithRawResponse:
    def __init__(self, entities: AsyncEntities) -> None:
        self._entities = entities

        self.ips = async_to_raw_response_wrapper(
            entities.ips,
        )

    @cached_property
    def asns(self) -> AsyncAsnsWithRawResponse:
        return AsyncAsnsWithRawResponse(self._entities.asns)


class EntitiesWithStreamingResponse:
    def __init__(self, entities: Entities) -> None:
        self._entities = entities

        self.ips = to_streamed_response_wrapper(
            entities.ips,
        )

    @cached_property
    def asns(self) -> AsnsWithStreamingResponse:
        return AsnsWithStreamingResponse(self._entities.asns)


class AsyncEntitiesWithStreamingResponse:
    def __init__(self, entities: AsyncEntities) -> None:
        self._entities = entities

        self.ips = async_to_streamed_response_wrapper(
            entities.ips,
        )

    @cached_property
    def asns(self) -> AsyncAsnsWithStreamingResponse:
        return AsyncAsnsWithStreamingResponse(self._entities.asns)
