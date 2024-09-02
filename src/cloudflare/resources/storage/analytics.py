# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.storage.schema import Schema

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ..._base_client import make_request_options

from ...types.storage.components import Components

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

from ...types.storage import analytics_list_params, analytics_stored_params

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types.storage import analytics_list_params
from ...types.storage import analytics_stored_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["AnalyticsResource", "AsyncAnalyticsResource"]


class AnalyticsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnalyticsResourceWithRawResponse:
        return AnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalyticsResourceWithStreamingResponse:
        return AnalyticsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        query: analytics_list_params.Query | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Schema]:
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
                post_parser=ResultWrapper[Optional[Schema]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Schema]], ResultWrapper[Schema]),
        )

    def stored(
        self,
        *,
        account_id: str,
        query: analytics_stored_params.Query | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Components]:
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
                post_parser=ResultWrapper[Optional[Components]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Components]], ResultWrapper[Components]),
        )


class AsyncAnalyticsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnalyticsResourceWithRawResponse:
        return AsyncAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        return AsyncAnalyticsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: str,
        query: analytics_list_params.Query | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Schema]:
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
                query=await async_maybe_transform({"query": query}, analytics_list_params.AnalyticsListParams),
                post_parser=ResultWrapper[Optional[Schema]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Schema]], ResultWrapper[Schema]),
        )

    async def stored(
        self,
        *,
        account_id: str,
        query: analytics_stored_params.Query | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Components]:
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
                query=await async_maybe_transform({"query": query}, analytics_stored_params.AnalyticsStoredParams),
                post_parser=ResultWrapper[Optional[Components]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Components]], ResultWrapper[Components]),
        )


class AnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

        self.list = to_raw_response_wrapper(
            analytics.list,
        )
        self.stored = to_raw_response_wrapper(
            analytics.stored,
        )


class AsyncAnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

        self.list = async_to_raw_response_wrapper(
            analytics.list,
        )
        self.stored = async_to_raw_response_wrapper(
            analytics.stored,
        )


class AnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

        self.list = to_streamed_response_wrapper(
            analytics.list,
        )
        self.stored = to_streamed_response_wrapper(
            analytics.stored,
        )


class AsyncAnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

        self.list = async_to_streamed_response_wrapper(
            analytics.list,
        )
        self.stored = async_to_streamed_response_wrapper(
            analytics.stored,
        )
