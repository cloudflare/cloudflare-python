# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.storage import (
    AnalyticsListResponse,
    AnalyticsStoredResponse,
    analytics_list_params,
    analytics_stored_params,
)

from typing import Type

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.storage import analytics_list_params
from ...types.storage import analytics_stored_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Analytics", "AsyncAnalytics"]


class Analytics(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnalyticsWithRawResponse:
        return AnalyticsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalyticsWithStreamingResponse:
        return AnalyticsWithStreamingResponse(self)

    def list(
        self,
        account_id: str,
        *,
        query: analytics_list_params.Query | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnalyticsListResponse:
        """
        Retrieves Workers KV request metrics for the given account.

        Args:
          account_id: Identifier

          query: For specifying result metrics.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/storage/analytics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"query": query}, analytics_list_params.AnalyticsListParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AnalyticsListResponse], ResultWrapper[AnalyticsListResponse]),
        )

    def stored(
        self,
        account_id: str,
        *,
        query: analytics_stored_params.Query | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnalyticsStoredResponse:
        """
        Retrieves Workers KV stored data metrics for the given account.

        Args:
          account_id: Identifier

          query: For specifying result metrics.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/storage/analytics/stored",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"query": query}, analytics_stored_params.AnalyticsStoredParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AnalyticsStoredResponse], ResultWrapper[AnalyticsStoredResponse]),
        )


class AsyncAnalytics(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnalyticsWithRawResponse:
        return AsyncAnalyticsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalyticsWithStreamingResponse:
        return AsyncAnalyticsWithStreamingResponse(self)

    async def list(
        self,
        account_id: str,
        *,
        query: analytics_list_params.Query | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnalyticsListResponse:
        """
        Retrieves Workers KV request metrics for the given account.

        Args:
          account_id: Identifier

          query: For specifying result metrics.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/storage/analytics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"query": query}, analytics_list_params.AnalyticsListParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AnalyticsListResponse], ResultWrapper[AnalyticsListResponse]),
        )

    async def stored(
        self,
        account_id: str,
        *,
        query: analytics_stored_params.Query | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnalyticsStoredResponse:
        """
        Retrieves Workers KV stored data metrics for the given account.

        Args:
          account_id: Identifier

          query: For specifying result metrics.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/storage/analytics/stored",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"query": query}, analytics_stored_params.AnalyticsStoredParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AnalyticsStoredResponse], ResultWrapper[AnalyticsStoredResponse]),
        )


class AnalyticsWithRawResponse:
    def __init__(self, analytics: Analytics) -> None:
        self._analytics = analytics

        self.list = to_raw_response_wrapper(
            analytics.list,
        )
        self.stored = to_raw_response_wrapper(
            analytics.stored,
        )


class AsyncAnalyticsWithRawResponse:
    def __init__(self, analytics: AsyncAnalytics) -> None:
        self._analytics = analytics

        self.list = async_to_raw_response_wrapper(
            analytics.list,
        )
        self.stored = async_to_raw_response_wrapper(
            analytics.stored,
        )


class AnalyticsWithStreamingResponse:
    def __init__(self, analytics: Analytics) -> None:
        self._analytics = analytics

        self.list = to_streamed_response_wrapper(
            analytics.list,
        )
        self.stored = to_streamed_response_wrapper(
            analytics.stored,
        )


class AsyncAnalyticsWithStreamingResponse:
    def __init__(self, analytics: AsyncAnalytics) -> None:
        self._analytics = analytics

        self.list = async_to_streamed_response_wrapper(
            analytics.list,
        )
        self.stored = async_to_streamed_response_wrapper(
            analytics.stored,
        )
