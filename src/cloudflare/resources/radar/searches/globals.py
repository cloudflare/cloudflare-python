# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.radar.searches import GlobalListResponse

from typing import Type, List

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
from ....types.radar.searches import global_list_params
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Globals", "AsyncGlobals"]


class Globals(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GlobalsWithRawResponse:
        return GlobalsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GlobalsWithStreamingResponse:
        return GlobalsWithStreamingResponse(self)

    def list(
        self,
        *,
        query: str,
        exclude: List[Literal["SPECIAL_EVENTS", "NOTEBOOKS", "LOCATIONS", "ASNS"]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        include: List[Literal["SPECIAL_EVENTS", "NOTEBOOKS", "LOCATIONS", "ASNS"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        limit_per_group: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalListResponse:
        """
        Lets you search for locations, autonomous systems (AS) and reports.

        Args:
          query: Search for locations, AS and reports.

          exclude: Search types to be excluded from results.

          format: Format results are returned in.

          include: Search types to be included in results.

          limit: Limit the number of objects in the response.

          limit_per_group: Limit the number of objects per search category.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/search/global",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query": query,
                        "exclude": exclude,
                        "format": format,
                        "include": include,
                        "limit": limit,
                        "limit_per_group": limit_per_group,
                    },
                    global_list_params.GlobalListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[GlobalListResponse], ResultWrapper[GlobalListResponse]),
        )


class AsyncGlobals(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGlobalsWithRawResponse:
        return AsyncGlobalsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGlobalsWithStreamingResponse:
        return AsyncGlobalsWithStreamingResponse(self)

    async def list(
        self,
        *,
        query: str,
        exclude: List[Literal["SPECIAL_EVENTS", "NOTEBOOKS", "LOCATIONS", "ASNS"]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        include: List[Literal["SPECIAL_EVENTS", "NOTEBOOKS", "LOCATIONS", "ASNS"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        limit_per_group: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalListResponse:
        """
        Lets you search for locations, autonomous systems (AS) and reports.

        Args:
          query: Search for locations, AS and reports.

          exclude: Search types to be excluded from results.

          format: Format results are returned in.

          include: Search types to be included in results.

          limit: Limit the number of objects in the response.

          limit_per_group: Limit the number of objects per search category.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/search/global",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query": query,
                        "exclude": exclude,
                        "format": format,
                        "include": include,
                        "limit": limit,
                        "limit_per_group": limit_per_group,
                    },
                    global_list_params.GlobalListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[GlobalListResponse], ResultWrapper[GlobalListResponse]),
        )


class GlobalsWithRawResponse:
    def __init__(self, globals: Globals) -> None:
        self._globals = globals

        self.list = to_raw_response_wrapper(
            globals.list,
        )


class AsyncGlobalsWithRawResponse:
    def __init__(self, globals: AsyncGlobals) -> None:
        self._globals = globals

        self.list = async_to_raw_response_wrapper(
            globals.list,
        )


class GlobalsWithStreamingResponse:
    def __init__(self, globals: Globals) -> None:
        self._globals = globals

        self.list = to_streamed_response_wrapper(
            globals.list,
        )


class AsyncGlobalsWithStreamingResponse:
    def __init__(self, globals: AsyncGlobals) -> None:
        self._globals = globals

        self.list = async_to_streamed_response_wrapper(
            globals.list,
        )
