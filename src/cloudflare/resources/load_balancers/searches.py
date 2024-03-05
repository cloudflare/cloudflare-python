# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.load_balancers import SearchGetResponse, search_get_params

__all__ = ["Searches", "AsyncSearches"]


class Searches(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SearchesWithRawResponse:
        return SearchesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchesWithStreamingResponse:
        return SearchesWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: str,
        page: object | NotGiven = NOT_GIVEN,
        per_page: object | NotGiven = NOT_GIVEN,
        search_params: search_get_params.SearchParams | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SearchGetResponse]:
        """
        Search for Load Balancing resources.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/load_balancers/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "search_params": search_params,
                    },
                    search_get_params.SearchGetParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SearchGetResponse]], ResultWrapper[SearchGetResponse]),
        )


class AsyncSearches(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSearchesWithRawResponse:
        return AsyncSearchesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchesWithStreamingResponse:
        return AsyncSearchesWithStreamingResponse(self)

    async def get(
        self,
        *,
        account_id: str,
        page: object | NotGiven = NOT_GIVEN,
        per_page: object | NotGiven = NOT_GIVEN,
        search_params: search_get_params.SearchParams | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SearchGetResponse]:
        """
        Search for Load Balancing resources.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/load_balancers/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "search_params": search_params,
                    },
                    search_get_params.SearchGetParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SearchGetResponse]], ResultWrapper[SearchGetResponse]),
        )


class SearchesWithRawResponse:
    def __init__(self, searches: Searches) -> None:
        self._searches = searches

        self.get = to_raw_response_wrapper(
            searches.get,
        )


class AsyncSearchesWithRawResponse:
    def __init__(self, searches: AsyncSearches) -> None:
        self._searches = searches

        self.get = async_to_raw_response_wrapper(
            searches.get,
        )


class SearchesWithStreamingResponse:
    def __init__(self, searches: Searches) -> None:
        self._searches = searches

        self.get = to_streamed_response_wrapper(
            searches.get,
        )


class AsyncSearchesWithStreamingResponse:
    def __init__(self, searches: AsyncSearches) -> None:
        self._searches = searches

        self.get = async_to_streamed_response_wrapper(
            searches.get,
        )
