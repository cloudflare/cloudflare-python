# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.intel import (
    IndicatorFeedCreateResponse,
    IndicatorFeedListResponse,
    IndicatorFeedDataResponse,
    IndicatorFeedGetResponse,
    IndicatorFeedPermissionsAddResponse,
    IndicatorFeedPermissionsRemoveResponse,
    IndicatorFeedPermissionsViewResponse,
    IndicatorFeedSnapshotResponse,
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
from ...types.intel import indicator_feed_create_params
from ...types.intel import indicator_feed_permissions_add_params
from ...types.intel import indicator_feed_permissions_remove_params
from ...types.intel import indicator_feed_snapshot_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["IndicatorFeeds", "AsyncIndicatorFeeds"]


class IndicatorFeeds(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IndicatorFeedsWithRawResponse:
        return IndicatorFeedsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndicatorFeedsWithStreamingResponse:
        return IndicatorFeedsWithStreamingResponse(self)

    def create(
        self,
        account_identifier: str,
        *,
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
          account_identifier: Identifier

          description: The description of the example test

          name: The name of the indicator feed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._post(
            f"/accounts/{account_identifier}/intel/indicator-feeds",
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IndicatorFeedCreateResponse], ResultWrapper[IndicatorFeedCreateResponse]),
        )

    def list(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndicatorFeedListResponse:
        """
        Get indicator feeds owned by this account

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/intel/indicator-feeds",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IndicatorFeedListResponse], ResultWrapper[IndicatorFeedListResponse]),
        )

    def data(
        self,
        feed_id: int,
        *,
        account_identifier: str,
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
          account_identifier: Identifier

          feed_id: Indicator feed ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        extra_headers = {"Accept": "text/csv", **(extra_headers or {})}
        return self._get(
            f"/accounts/{account_identifier}/intel/indicator-feeds/{feed_id}/data",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def get(
        self,
        feed_id: int,
        *,
        account_identifier: str,
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
          account_identifier: Identifier

          feed_id: Indicator feed ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/intel/indicator-feeds/{feed_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IndicatorFeedGetResponse], ResultWrapper[IndicatorFeedGetResponse]),
        )

    def permissions_add(
        self,
        account_identifier: str,
        *,
        account_tag: str | NotGiven = NOT_GIVEN,
        feed_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndicatorFeedPermissionsAddResponse:
        """
        Grant permission to indicator feed

        Args:
          account_identifier: Identifier

          account_tag: The Cloudflare account tag of the account to change permissions on

          feed_id: The ID of the feed to add/remove permissions on

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._put(
            f"/accounts/{account_identifier}/intel/indicator-feeds/permissions/add",
            body=maybe_transform(
                {
                    "account_tag": account_tag,
                    "feed_id": feed_id,
                },
                indicator_feed_permissions_add_params.IndicatorFeedPermissionsAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IndicatorFeedPermissionsAddResponse], ResultWrapper[IndicatorFeedPermissionsAddResponse]),
        )

    def permissions_remove(
        self,
        account_identifier: str,
        *,
        account_tag: str | NotGiven = NOT_GIVEN,
        feed_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndicatorFeedPermissionsRemoveResponse:
        """
        Revoke permission to indicator feed

        Args:
          account_identifier: Identifier

          account_tag: The Cloudflare account tag of the account to change permissions on

          feed_id: The ID of the feed to add/remove permissions on

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._put(
            f"/accounts/{account_identifier}/intel/indicator-feeds/permissions/remove",
            body=maybe_transform(
                {
                    "account_tag": account_tag,
                    "feed_id": feed_id,
                },
                indicator_feed_permissions_remove_params.IndicatorFeedPermissionsRemoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[IndicatorFeedPermissionsRemoveResponse], ResultWrapper[IndicatorFeedPermissionsRemoveResponse]
            ),
        )

    def permissions_view(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndicatorFeedPermissionsViewResponse:
        """
        List indicator feed permissions

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/intel/indicator-feeds/permissions/view",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[IndicatorFeedPermissionsViewResponse], ResultWrapper[IndicatorFeedPermissionsViewResponse]
            ),
        )

    def snapshot(
        self,
        feed_id: int,
        *,
        account_identifier: str,
        source: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndicatorFeedSnapshotResponse:
        """
        Update indicator feed data

        Args:
          account_identifier: Identifier

          feed_id: Indicator feed ID

          source: The file to upload

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._put(
            f"/accounts/{account_identifier}/intel/indicator-feeds/{feed_id}/snapshot",
            body=maybe_transform({"source": source}, indicator_feed_snapshot_params.IndicatorFeedSnapshotParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IndicatorFeedSnapshotResponse], ResultWrapper[IndicatorFeedSnapshotResponse]),
        )


class AsyncIndicatorFeeds(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIndicatorFeedsWithRawResponse:
        return AsyncIndicatorFeedsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndicatorFeedsWithStreamingResponse:
        return AsyncIndicatorFeedsWithStreamingResponse(self)

    async def create(
        self,
        account_identifier: str,
        *,
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
          account_identifier: Identifier

          description: The description of the example test

          name: The name of the indicator feed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._post(
            f"/accounts/{account_identifier}/intel/indicator-feeds",
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IndicatorFeedCreateResponse], ResultWrapper[IndicatorFeedCreateResponse]),
        )

    async def list(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndicatorFeedListResponse:
        """
        Get indicator feeds owned by this account

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/intel/indicator-feeds",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IndicatorFeedListResponse], ResultWrapper[IndicatorFeedListResponse]),
        )

    async def data(
        self,
        feed_id: int,
        *,
        account_identifier: str,
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
          account_identifier: Identifier

          feed_id: Indicator feed ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        extra_headers = {"Accept": "text/csv", **(extra_headers or {})}
        return await self._get(
            f"/accounts/{account_identifier}/intel/indicator-feeds/{feed_id}/data",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def get(
        self,
        feed_id: int,
        *,
        account_identifier: str,
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
          account_identifier: Identifier

          feed_id: Indicator feed ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/intel/indicator-feeds/{feed_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IndicatorFeedGetResponse], ResultWrapper[IndicatorFeedGetResponse]),
        )

    async def permissions_add(
        self,
        account_identifier: str,
        *,
        account_tag: str | NotGiven = NOT_GIVEN,
        feed_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndicatorFeedPermissionsAddResponse:
        """
        Grant permission to indicator feed

        Args:
          account_identifier: Identifier

          account_tag: The Cloudflare account tag of the account to change permissions on

          feed_id: The ID of the feed to add/remove permissions on

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._put(
            f"/accounts/{account_identifier}/intel/indicator-feeds/permissions/add",
            body=maybe_transform(
                {
                    "account_tag": account_tag,
                    "feed_id": feed_id,
                },
                indicator_feed_permissions_add_params.IndicatorFeedPermissionsAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IndicatorFeedPermissionsAddResponse], ResultWrapper[IndicatorFeedPermissionsAddResponse]),
        )

    async def permissions_remove(
        self,
        account_identifier: str,
        *,
        account_tag: str | NotGiven = NOT_GIVEN,
        feed_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndicatorFeedPermissionsRemoveResponse:
        """
        Revoke permission to indicator feed

        Args:
          account_identifier: Identifier

          account_tag: The Cloudflare account tag of the account to change permissions on

          feed_id: The ID of the feed to add/remove permissions on

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._put(
            f"/accounts/{account_identifier}/intel/indicator-feeds/permissions/remove",
            body=maybe_transform(
                {
                    "account_tag": account_tag,
                    "feed_id": feed_id,
                },
                indicator_feed_permissions_remove_params.IndicatorFeedPermissionsRemoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[IndicatorFeedPermissionsRemoveResponse], ResultWrapper[IndicatorFeedPermissionsRemoveResponse]
            ),
        )

    async def permissions_view(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndicatorFeedPermissionsViewResponse:
        """
        List indicator feed permissions

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/intel/indicator-feeds/permissions/view",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[IndicatorFeedPermissionsViewResponse], ResultWrapper[IndicatorFeedPermissionsViewResponse]
            ),
        )

    async def snapshot(
        self,
        feed_id: int,
        *,
        account_identifier: str,
        source: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndicatorFeedSnapshotResponse:
        """
        Update indicator feed data

        Args:
          account_identifier: Identifier

          feed_id: Indicator feed ID

          source: The file to upload

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._put(
            f"/accounts/{account_identifier}/intel/indicator-feeds/{feed_id}/snapshot",
            body=maybe_transform({"source": source}, indicator_feed_snapshot_params.IndicatorFeedSnapshotParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IndicatorFeedSnapshotResponse], ResultWrapper[IndicatorFeedSnapshotResponse]),
        )


class IndicatorFeedsWithRawResponse:
    def __init__(self, indicator_feeds: IndicatorFeeds) -> None:
        self._indicator_feeds = indicator_feeds

        self.create = to_raw_response_wrapper(
            indicator_feeds.create,
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
        self.permissions_add = to_raw_response_wrapper(
            indicator_feeds.permissions_add,
        )
        self.permissions_remove = to_raw_response_wrapper(
            indicator_feeds.permissions_remove,
        )
        self.permissions_view = to_raw_response_wrapper(
            indicator_feeds.permissions_view,
        )
        self.snapshot = to_raw_response_wrapper(
            indicator_feeds.snapshot,
        )


class AsyncIndicatorFeedsWithRawResponse:
    def __init__(self, indicator_feeds: AsyncIndicatorFeeds) -> None:
        self._indicator_feeds = indicator_feeds

        self.create = async_to_raw_response_wrapper(
            indicator_feeds.create,
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
        self.permissions_add = async_to_raw_response_wrapper(
            indicator_feeds.permissions_add,
        )
        self.permissions_remove = async_to_raw_response_wrapper(
            indicator_feeds.permissions_remove,
        )
        self.permissions_view = async_to_raw_response_wrapper(
            indicator_feeds.permissions_view,
        )
        self.snapshot = async_to_raw_response_wrapper(
            indicator_feeds.snapshot,
        )


class IndicatorFeedsWithStreamingResponse:
    def __init__(self, indicator_feeds: IndicatorFeeds) -> None:
        self._indicator_feeds = indicator_feeds

        self.create = to_streamed_response_wrapper(
            indicator_feeds.create,
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
        self.permissions_add = to_streamed_response_wrapper(
            indicator_feeds.permissions_add,
        )
        self.permissions_remove = to_streamed_response_wrapper(
            indicator_feeds.permissions_remove,
        )
        self.permissions_view = to_streamed_response_wrapper(
            indicator_feeds.permissions_view,
        )
        self.snapshot = to_streamed_response_wrapper(
            indicator_feeds.snapshot,
        )


class AsyncIndicatorFeedsWithStreamingResponse:
    def __init__(self, indicator_feeds: AsyncIndicatorFeeds) -> None:
        self._indicator_feeds = indicator_feeds

        self.create = async_to_streamed_response_wrapper(
            indicator_feeds.create,
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
        self.permissions_add = async_to_streamed_response_wrapper(
            indicator_feeds.permissions_add,
        )
        self.permissions_remove = async_to_streamed_response_wrapper(
            indicator_feeds.permissions_remove,
        )
        self.permissions_view = async_to_streamed_response_wrapper(
            indicator_feeds.permissions_view,
        )
        self.snapshot = async_to_streamed_response_wrapper(
            indicator_feeds.snapshot,
        )
