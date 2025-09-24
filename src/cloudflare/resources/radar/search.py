# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.radar import search_global_params
from ..._base_client import make_request_options
from ...types.radar.search_global_response import SearchGlobalResponse

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SearchResourceWithStreamingResponse(self)

    def global_(
        self,
        *,
        query: str,
        exclude: List[
            Literal[
                "ADM1S",
                "ASNS",
                "BOTS",
                "CERTIFICATE_AUTHORITIES",
                "CERTIFICATE_LOGS",
                "INDUSTRIES",
                "LOCATIONS",
                "NOTEBOOKS",
                "TLDS",
                "VERTICALS",
            ]
        ]
        | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        include: List[
            Literal[
                "ADM1S",
                "ASNS",
                "BOTS",
                "CERTIFICATE_AUTHORITIES",
                "CERTIFICATE_LOGS",
                "INDUSTRIES",
                "LOCATIONS",
                "NOTEBOOKS",
                "TLDS",
                "VERTICALS",
            ]
        ]
        | Omit = omit,
        limit: int | Omit = omit,
        limit_per_group: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchGlobalResponse:
        """
        Searches for locations, autonomous systems, reports, bots, certificate logs,
        certificate authorities, industries and verticals

        Args:
          query: String used to perform the search operation.

          exclude: Search types excluded from results.

          format: Format in which results will be returned.

          include: Search types included in results.

          limit: Limits the number of objects returned in the response.

          limit_per_group: Limits the number of objects per search category.

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
                    search_global_params.SearchGlobalParams,
                ),
                post_parser=ResultWrapper[SearchGlobalResponse]._unwrapper,
            ),
            cast_to=cast(Type[SearchGlobalResponse], ResultWrapper[SearchGlobalResponse]),
        )


class AsyncSearchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSearchResourceWithStreamingResponse(self)

    async def global_(
        self,
        *,
        query: str,
        exclude: List[
            Literal[
                "ADM1S",
                "ASNS",
                "BOTS",
                "CERTIFICATE_AUTHORITIES",
                "CERTIFICATE_LOGS",
                "INDUSTRIES",
                "LOCATIONS",
                "NOTEBOOKS",
                "TLDS",
                "VERTICALS",
            ]
        ]
        | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        include: List[
            Literal[
                "ADM1S",
                "ASNS",
                "BOTS",
                "CERTIFICATE_AUTHORITIES",
                "CERTIFICATE_LOGS",
                "INDUSTRIES",
                "LOCATIONS",
                "NOTEBOOKS",
                "TLDS",
                "VERTICALS",
            ]
        ]
        | Omit = omit,
        limit: int | Omit = omit,
        limit_per_group: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchGlobalResponse:
        """
        Searches for locations, autonomous systems, reports, bots, certificate logs,
        certificate authorities, industries and verticals

        Args:
          query: String used to perform the search operation.

          exclude: Search types excluded from results.

          format: Format in which results will be returned.

          include: Search types included in results.

          limit: Limits the number of objects returned in the response.

          limit_per_group: Limits the number of objects per search category.

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
                query=await async_maybe_transform(
                    {
                        "query": query,
                        "exclude": exclude,
                        "format": format,
                        "include": include,
                        "limit": limit,
                        "limit_per_group": limit_per_group,
                    },
                    search_global_params.SearchGlobalParams,
                ),
                post_parser=ResultWrapper[SearchGlobalResponse]._unwrapper,
            ),
            cast_to=cast(Type[SearchGlobalResponse], ResultWrapper[SearchGlobalResponse]),
        )


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.global_ = to_raw_response_wrapper(
            search.global_,
        )


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.global_ = async_to_raw_response_wrapper(
            search.global_,
        )


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.global_ = to_streamed_response_wrapper(
            search.global_,
        )


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.global_ = async_to_streamed_response_wrapper(
            search.global_,
        )
