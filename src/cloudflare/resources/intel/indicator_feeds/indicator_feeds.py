# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from .permissions import (
    PermissionsResource,
    AsyncPermissionsResource,
    PermissionsResourceWithRawResponse,
    AsyncPermissionsResourceWithRawResponse,
    PermissionsResourceWithStreamingResponse,
    AsyncPermissionsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from ....types.intel import indicator_feed_create_params, indicator_feed_update_params
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ....types.intel.indicator_feed_get_response import IndicatorFeedGetResponse
from ....types.intel.indicator_feed_list_response import IndicatorFeedListResponse
from ....types.intel.indicator_feed_create_response import IndicatorFeedCreateResponse
from ....types.intel.indicator_feed_update_response import IndicatorFeedUpdateResponse

__all__ = ["IndicatorFeedsResource", "AsyncIndicatorFeedsResource"]


class IndicatorFeedsResource(SyncAPIResource):
    @cached_property
    def permissions(self) -> PermissionsResource:
        return PermissionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> IndicatorFeedsResourceWithRawResponse:
        return IndicatorFeedsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndicatorFeedsResourceWithStreamingResponse:
        return IndicatorFeedsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndicatorFeedCreateResponse:
        """
        Create new indicator feed

        Args:
          account_id: Identifier

          description: The description of the example test

          name: The name of the indicator feed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/intel/indicator-feeds",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                indicator_feed_create_params.IndicatorFeedCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[IndicatorFeedCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[IndicatorFeedCreateResponse], ResultWrapper[IndicatorFeedCreateResponse]),
        )

    def update(
        self,
        feed_id: int,
        *,
        account_id: str,
        source: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndicatorFeedUpdateResponse:
        """
        Update indicator feed data

        Args:
          account_id: Identifier

          feed_id: Indicator feed ID

          source: The file to upload

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._put(
            f"/accounts/{account_id}/intel/indicator-feeds/{feed_id}/snapshot",
            body=maybe_transform({"source": source}, indicator_feed_update_params.IndicatorFeedUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[IndicatorFeedUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[IndicatorFeedUpdateResponse], ResultWrapper[IndicatorFeedUpdateResponse]),
        )

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
    ) -> SyncSinglePage[IndicatorFeedListResponse]:
        """
        Get indicator feeds owned by this account

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
            f"/accounts/{account_id}/intel/indicator-feeds",
            page=SyncSinglePage[IndicatorFeedListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=IndicatorFeedListResponse,
        )

    def data(
        self,
        feed_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Get indicator feed data

        Args:
          account_id: Identifier

          feed_id: Indicator feed ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {"Accept": "text/csv", **(extra_headers or {})}
        return self._get(
            f"/accounts/{account_id}/intel/indicator-feeds/{feed_id}/data",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def get(
        self,
        feed_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndicatorFeedGetResponse:
        """
        Get indicator feed metadata

        Args:
          account_id: Identifier

          feed_id: Indicator feed ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/intel/indicator-feeds/{feed_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[IndicatorFeedGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[IndicatorFeedGetResponse], ResultWrapper[IndicatorFeedGetResponse]),
        )


class AsyncIndicatorFeedsResource(AsyncAPIResource):
    @cached_property
    def permissions(self) -> AsyncPermissionsResource:
        return AsyncPermissionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIndicatorFeedsResourceWithRawResponse:
        return AsyncIndicatorFeedsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndicatorFeedsResourceWithStreamingResponse:
        return AsyncIndicatorFeedsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndicatorFeedCreateResponse:
        """
        Create new indicator feed

        Args:
          account_id: Identifier

          description: The description of the example test

          name: The name of the indicator feed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/intel/indicator-feeds",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                indicator_feed_create_params.IndicatorFeedCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[IndicatorFeedCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[IndicatorFeedCreateResponse], ResultWrapper[IndicatorFeedCreateResponse]),
        )

    async def update(
        self,
        feed_id: int,
        *,
        account_id: str,
        source: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndicatorFeedUpdateResponse:
        """
        Update indicator feed data

        Args:
          account_id: Identifier

          feed_id: Indicator feed ID

          source: The file to upload

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._put(
            f"/accounts/{account_id}/intel/indicator-feeds/{feed_id}/snapshot",
            body=await async_maybe_transform(
                {"source": source}, indicator_feed_update_params.IndicatorFeedUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[IndicatorFeedUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[IndicatorFeedUpdateResponse], ResultWrapper[IndicatorFeedUpdateResponse]),
        )

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
    ) -> AsyncPaginator[IndicatorFeedListResponse, AsyncSinglePage[IndicatorFeedListResponse]]:
        """
        Get indicator feeds owned by this account

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
            f"/accounts/{account_id}/intel/indicator-feeds",
            page=AsyncSinglePage[IndicatorFeedListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=IndicatorFeedListResponse,
        )

    async def data(
        self,
        feed_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Get indicator feed data

        Args:
          account_id: Identifier

          feed_id: Indicator feed ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {"Accept": "text/csv", **(extra_headers or {})}
        return await self._get(
            f"/accounts/{account_id}/intel/indicator-feeds/{feed_id}/data",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def get(
        self,
        feed_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndicatorFeedGetResponse:
        """
        Get indicator feed metadata

        Args:
          account_id: Identifier

          feed_id: Indicator feed ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/intel/indicator-feeds/{feed_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[IndicatorFeedGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[IndicatorFeedGetResponse], ResultWrapper[IndicatorFeedGetResponse]),
        )


class IndicatorFeedsResourceWithRawResponse:
    def __init__(self, indicator_feeds: IndicatorFeedsResource) -> None:
        self._indicator_feeds = indicator_feeds

        self.create = to_raw_response_wrapper(
            indicator_feeds.create,
        )
        self.update = to_raw_response_wrapper(
            indicator_feeds.update,
        )
        self.list = to_raw_response_wrapper(
            indicator_feeds.list,
        )
        self.data = to_raw_response_wrapper(
            indicator_feeds.data,
        )
        self.get = to_raw_response_wrapper(
            indicator_feeds.get,
        )

    @cached_property
    def permissions(self) -> PermissionsResourceWithRawResponse:
        return PermissionsResourceWithRawResponse(self._indicator_feeds.permissions)


class AsyncIndicatorFeedsResourceWithRawResponse:
    def __init__(self, indicator_feeds: AsyncIndicatorFeedsResource) -> None:
        self._indicator_feeds = indicator_feeds

        self.create = async_to_raw_response_wrapper(
            indicator_feeds.create,
        )
        self.update = async_to_raw_response_wrapper(
            indicator_feeds.update,
        )
        self.list = async_to_raw_response_wrapper(
            indicator_feeds.list,
        )
        self.data = async_to_raw_response_wrapper(
            indicator_feeds.data,
        )
        self.get = async_to_raw_response_wrapper(
            indicator_feeds.get,
        )

    @cached_property
    def permissions(self) -> AsyncPermissionsResourceWithRawResponse:
        return AsyncPermissionsResourceWithRawResponse(self._indicator_feeds.permissions)


class IndicatorFeedsResourceWithStreamingResponse:
    def __init__(self, indicator_feeds: IndicatorFeedsResource) -> None:
        self._indicator_feeds = indicator_feeds

        self.create = to_streamed_response_wrapper(
            indicator_feeds.create,
        )
        self.update = to_streamed_response_wrapper(
            indicator_feeds.update,
        )
        self.list = to_streamed_response_wrapper(
            indicator_feeds.list,
        )
        self.data = to_streamed_response_wrapper(
            indicator_feeds.data,
        )
        self.get = to_streamed_response_wrapper(
            indicator_feeds.get,
        )

    @cached_property
    def permissions(self) -> PermissionsResourceWithStreamingResponse:
        return PermissionsResourceWithStreamingResponse(self._indicator_feeds.permissions)


class AsyncIndicatorFeedsResourceWithStreamingResponse:
    def __init__(self, indicator_feeds: AsyncIndicatorFeedsResource) -> None:
        self._indicator_feeds = indicator_feeds

        self.create = async_to_streamed_response_wrapper(
            indicator_feeds.create,
        )
        self.update = async_to_streamed_response_wrapper(
            indicator_feeds.update,
        )
        self.list = async_to_streamed_response_wrapper(
            indicator_feeds.list,
        )
        self.data = async_to_streamed_response_wrapper(
            indicator_feeds.data,
        )
        self.get = async_to_streamed_response_wrapper(
            indicator_feeds.get,
        )

    @cached_property
    def permissions(self) -> AsyncPermissionsResourceWithStreamingResponse:
        return AsyncPermissionsResourceWithStreamingResponse(self._indicator_feeds.permissions)
