# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.load_balancers.search_get_response import SearchGetResponse

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from ..._base_client import make_request_options

from typing import Type

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

from ...types.load_balancers import search_get_params

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types.load_balancers import search_get_params
from typing import cast
from typing import cast

__all__ = ["SearchesResource", "AsyncSearchesResource"]


class SearchesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SearchesResourceWithRawResponse:
        return SearchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchesResourceWithStreamingResponse:
        return SearchesResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: str,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        search_params: search_get_params.SearchParams | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchGetResponse:
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
                post_parser=ResultWrapper[SearchGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SearchGetResponse], ResultWrapper[SearchGetResponse]),
        )


class AsyncSearchesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSearchesResourceWithRawResponse:
        return AsyncSearchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchesResourceWithStreamingResponse:
        return AsyncSearchesResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        account_id: str,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        search_params: search_get_params.SearchParams | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchGetResponse:
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
                post_parser=ResultWrapper[SearchGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SearchGetResponse], ResultWrapper[SearchGetResponse]),
        )


class SearchesResourceWithRawResponse:
    def __init__(self, searches: SearchesResource) -> None:
        self._searches = searches

        self.get = to_raw_response_wrapper(
            searches.get,
        )


class AsyncSearchesResourceWithRawResponse:
    def __init__(self, searches: AsyncSearchesResource) -> None:
        self._searches = searches

        self.get = async_to_raw_response_wrapper(
            searches.get,
        )


class SearchesResourceWithStreamingResponse:
    def __init__(self, searches: SearchesResource) -> None:
        self._searches = searches

        self.get = to_streamed_response_wrapper(
            searches.get,
        )


class AsyncSearchesResourceWithStreamingResponse:
    def __init__(self, searches: AsyncSearchesResource) -> None:
        self._searches = searches

        self.get = async_to_streamed_response_wrapper(
            searches.get,
        )
