# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.radar.robots_txt.top.directive_get_response import DirectiveGetResponse

from ....._wrappers import ResultWrapper

from ....._utils import maybe_transform, async_maybe_transform

from ....._base_client import make_request_options

from typing import Type, List

from typing_extensions import Literal

from ....._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .....types.radar.robots_txt.top import directive_get_params
from typing import cast
from typing import cast

__all__ = ["DirectiveResource", "AsyncDirectiveResource"]


class DirectiveResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DirectiveResourceWithRawResponse:
        return DirectiveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DirectiveResourceWithStreamingResponse:
        return DirectiveResourceWithStreamingResponse(self)

    def get(
        self,
        directive: Literal["ALLOW", "DISALLOW"],
        *,
        agent_category: Literal["AI"] | NotGiven = NOT_GIVEN,
        date: str | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DirectiveGetResponse:
        """
        Get the top User-Agents on robots.txt files by directive.

        Args:
          directive: Robots.txt directive.

          agent_category: Filter by user agent category.

          date: Date to filter the ranking.

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          name: Array of names that will be used to name the series in responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not directive:
            raise ValueError(f"Expected a non-empty value for `directive` but received {directive!r}")
        return self._get(
            f"/radar/robots_txt/top/{directive}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agent_category": agent_category,
                        "date": date,
                        "format": format,
                        "limit": limit,
                        "name": name,
                    },
                    directive_get_params.DirectiveGetParams,
                ),
                post_parser=ResultWrapper[DirectiveGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[DirectiveGetResponse], ResultWrapper[DirectiveGetResponse]),
        )


class AsyncDirectiveResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDirectiveResourceWithRawResponse:
        return AsyncDirectiveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDirectiveResourceWithStreamingResponse:
        return AsyncDirectiveResourceWithStreamingResponse(self)

    async def get(
        self,
        directive: Literal["ALLOW", "DISALLOW"],
        *,
        agent_category: Literal["AI"] | NotGiven = NOT_GIVEN,
        date: str | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DirectiveGetResponse:
        """
        Get the top User-Agents on robots.txt files by directive.

        Args:
          directive: Robots.txt directive.

          agent_category: Filter by user agent category.

          date: Date to filter the ranking.

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          name: Array of names that will be used to name the series in responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not directive:
            raise ValueError(f"Expected a non-empty value for `directive` but received {directive!r}")
        return await self._get(
            f"/radar/robots_txt/top/{directive}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agent_category": agent_category,
                        "date": date,
                        "format": format,
                        "limit": limit,
                        "name": name,
                    },
                    directive_get_params.DirectiveGetParams,
                ),
                post_parser=ResultWrapper[DirectiveGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[DirectiveGetResponse], ResultWrapper[DirectiveGetResponse]),
        )


class DirectiveResourceWithRawResponse:
    def __init__(self, directive: DirectiveResource) -> None:
        self._directive = directive

        self.get = to_raw_response_wrapper(
            directive.get,
        )


class AsyncDirectiveResourceWithRawResponse:
    def __init__(self, directive: AsyncDirectiveResource) -> None:
        self._directive = directive

        self.get = async_to_raw_response_wrapper(
            directive.get,
        )


class DirectiveResourceWithStreamingResponse:
    def __init__(self, directive: DirectiveResource) -> None:
        self._directive = directive

        self.get = to_streamed_response_wrapper(
            directive.get,
        )


class AsyncDirectiveResourceWithStreamingResponse:
    def __init__(self, directive: AsyncDirectiveResource) -> None:
        self._directive = directive

        self.get = async_to_streamed_response_wrapper(
            directive.get,
        )
