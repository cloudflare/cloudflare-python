# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.zero_trust.gateway.category import Category

from ....pagination import SyncSinglePage, AsyncSinglePage

from ...._base_client import make_request_options, AsyncPaginator

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
from ....types import shared_params

__all__ = ["CategoriesResource", "AsyncCategoriesResource"]


class CategoriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CategoriesResourceWithRawResponse:
        return CategoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CategoriesResourceWithStreamingResponse:
        return CategoriesResourceWithStreamingResponse(self)

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
    ) -> SyncSinglePage[Category]:
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
        return self._get_api_list(
            f"/accounts/{account_id}/gateway/categories",
            page=SyncSinglePage[Category],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Category,
        )


class AsyncCategoriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCategoriesResourceWithRawResponse:
        return AsyncCategoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCategoriesResourceWithStreamingResponse:
        return AsyncCategoriesResourceWithStreamingResponse(self)

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
    ) -> AsyncPaginator[Category, AsyncSinglePage[Category]]:
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
        return self._get_api_list(
            f"/accounts/{account_id}/gateway/categories",
            page=AsyncSinglePage[Category],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Category,
        )


class CategoriesResourceWithRawResponse:
    def __init__(self, categories: CategoriesResource) -> None:
        self._categories = categories

        self.list = to_raw_response_wrapper(
            categories.list,
        )


class AsyncCategoriesResourceWithRawResponse:
    def __init__(self, categories: AsyncCategoriesResource) -> None:
        self._categories = categories

        self.list = async_to_raw_response_wrapper(
            categories.list,
        )


class CategoriesResourceWithStreamingResponse:
    def __init__(self, categories: CategoriesResource) -> None:
        self._categories = categories

        self.list = to_streamed_response_wrapper(
            categories.list,
        )


class AsyncCategoriesResourceWithStreamingResponse:
    def __init__(self, categories: AsyncCategoriesResource) -> None:
        self._categories = categories

        self.list = async_to_streamed_response_wrapper(
            categories.list,
        )
