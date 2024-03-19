# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.zero_trust.gateway import CategoryListResponse

__all__ = ["Categories", "AsyncCategories"]


class Categories(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CategoriesWithRawResponse:
        return CategoriesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CategoriesWithStreamingResponse:
        return CategoriesWithStreamingResponse(self)

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
    ) -> Optional[CategoryListResponse]:
        """
        Fetches a list of all categories.

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
            f"/accounts/{account_id}/gateway/categories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[CategoryListResponse]], ResultWrapper[CategoryListResponse]),
        )


class AsyncCategories(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCategoriesWithRawResponse:
        return AsyncCategoriesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCategoriesWithStreamingResponse:
        return AsyncCategoriesWithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CategoryListResponse]:
        """
        Fetches a list of all categories.

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
            f"/accounts/{account_id}/gateway/categories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[CategoryListResponse]], ResultWrapper[CategoryListResponse]),
        )


class CategoriesWithRawResponse:
    def __init__(self, categories: Categories) -> None:
        self._categories = categories

        self.list = to_raw_response_wrapper(
            categories.list,
        )


class AsyncCategoriesWithRawResponse:
    def __init__(self, categories: AsyncCategories) -> None:
        self._categories = categories

        self.list = async_to_raw_response_wrapper(
            categories.list,
        )


class CategoriesWithStreamingResponse:
    def __init__(self, categories: Categories) -> None:
        self._categories = categories

        self.list = to_streamed_response_wrapper(
            categories.list,
        )


class AsyncCategoriesWithStreamingResponse:
    def __init__(self, categories: AsyncCategories) -> None:
        self._categories = categories

        self.list = async_to_streamed_response_wrapper(
            categories.list,
        )
