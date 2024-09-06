# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.zero_trust.gateway.app_type import AppType

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
from typing import cast
from typing import cast

__all__ = ["AppTypesResource", "AsyncAppTypesResource"]


class AppTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AppTypesResourceWithRawResponse:
        return AppTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppTypesResourceWithStreamingResponse:
        return AppTypesResourceWithStreamingResponse(self)

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
    ) -> SyncSinglePage[AppType]:
        """
        Fetches all application and application type mappings.

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
            f"/accounts/{account_id}/gateway/app_types",
            page=SyncSinglePage[AppType],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=cast(Any, AppType),  # Union types cannot be passed in as arguments in the type system
        )


class AsyncAppTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAppTypesResourceWithRawResponse:
        return AsyncAppTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppTypesResourceWithStreamingResponse:
        return AsyncAppTypesResourceWithStreamingResponse(self)

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
    ) -> AsyncPaginator[AppType, AsyncSinglePage[AppType]]:
        """
        Fetches all application and application type mappings.

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
            f"/accounts/{account_id}/gateway/app_types",
            page=AsyncSinglePage[AppType],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=cast(Any, AppType),  # Union types cannot be passed in as arguments in the type system
        )


class AppTypesResourceWithRawResponse:
    def __init__(self, app_types: AppTypesResource) -> None:
        self._app_types = app_types

        self.list = to_raw_response_wrapper(
            app_types.list,
        )


class AsyncAppTypesResourceWithRawResponse:
    def __init__(self, app_types: AsyncAppTypesResource) -> None:
        self._app_types = app_types

        self.list = async_to_raw_response_wrapper(
            app_types.list,
        )


class AppTypesResourceWithStreamingResponse:
    def __init__(self, app_types: AppTypesResource) -> None:
        self._app_types = app_types

        self.list = to_streamed_response_wrapper(
            app_types.list,
        )


class AsyncAppTypesResourceWithStreamingResponse:
    def __init__(self, app_types: AsyncAppTypesResource) -> None:
        self._app_types = app_types

        self.list = async_to_streamed_response_wrapper(
            app_types.list,
        )
