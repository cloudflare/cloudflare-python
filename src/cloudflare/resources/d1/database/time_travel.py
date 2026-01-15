# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, cast
from datetime import datetime

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.d1.database import time_travel_restore_params, time_travel_get_bookmark_params
from ....types.d1.database.time_travel_restore_response import TimeTravelRestoreResponse
from ....types.d1.database.time_travel_get_bookmark_response import TimeTravelGetBookmarkResponse

__all__ = ["TimeTravelResource", "AsyncTimeTravelResource"]


class TimeTravelResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TimeTravelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TimeTravelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TimeTravelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TimeTravelResourceWithStreamingResponse(self)

    def get_bookmark(
        self,
        database_id: str,
        *,
        account_id: str,
        timestamp: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeTravelGetBookmarkResponse:
        """
        Retrieves the current bookmark, or the nearest bookmark at or before a provided
        timestamp. Bookmarks can be used with the restore endpoint to revert the
        database to a previous point in time.

        Args:
          account_id: Account identifier tag.

          database_id: D1 database identifier (UUID).

          timestamp: An optional ISO 8601 timestamp. If provided, returns the nearest available
              bookmark at or before this timestamp. If omitted, returns the current bookmark.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not database_id:
            raise ValueError(f"Expected a non-empty value for `database_id` but received {database_id!r}")
        return self._get(
            f"/accounts/{account_id}/d1/database/{database_id}/time_travel/bookmark",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"timestamp": timestamp}, time_travel_get_bookmark_params.TimeTravelGetBookmarkParams
                ),
                post_parser=ResultWrapper[TimeTravelGetBookmarkResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeTravelGetBookmarkResponse], ResultWrapper[TimeTravelGetBookmarkResponse]),
        )

    def restore(
        self,
        database_id: str,
        *,
        account_id: str,
        bookmark: str | Omit = omit,
        timestamp: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeTravelRestoreResponse:
        """
        Restores a D1 database to a previous point in time either via a bookmark or a
        timestamp.

        Args:
          account_id: Account identifier tag.

          database_id: D1 database identifier (UUID).

          bookmark: A bookmark to restore the database to. Required if `timestamp` is not provided.

          timestamp: An ISO 8601 timestamp to restore the database to. Required if `bookmark` is not
              provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not database_id:
            raise ValueError(f"Expected a non-empty value for `database_id` but received {database_id!r}")
        return self._post(
            f"/accounts/{account_id}/d1/database/{database_id}/time_travel/restore",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "bookmark": bookmark,
                        "timestamp": timestamp,
                    },
                    time_travel_restore_params.TimeTravelRestoreParams,
                ),
                post_parser=ResultWrapper[TimeTravelRestoreResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeTravelRestoreResponse], ResultWrapper[TimeTravelRestoreResponse]),
        )


class AsyncTimeTravelResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTimeTravelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTimeTravelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTimeTravelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTimeTravelResourceWithStreamingResponse(self)

    async def get_bookmark(
        self,
        database_id: str,
        *,
        account_id: str,
        timestamp: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeTravelGetBookmarkResponse:
        """
        Retrieves the current bookmark, or the nearest bookmark at or before a provided
        timestamp. Bookmarks can be used with the restore endpoint to revert the
        database to a previous point in time.

        Args:
          account_id: Account identifier tag.

          database_id: D1 database identifier (UUID).

          timestamp: An optional ISO 8601 timestamp. If provided, returns the nearest available
              bookmark at or before this timestamp. If omitted, returns the current bookmark.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not database_id:
            raise ValueError(f"Expected a non-empty value for `database_id` but received {database_id!r}")
        return await self._get(
            f"/accounts/{account_id}/d1/database/{database_id}/time_travel/bookmark",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"timestamp": timestamp}, time_travel_get_bookmark_params.TimeTravelGetBookmarkParams
                ),
                post_parser=ResultWrapper[TimeTravelGetBookmarkResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeTravelGetBookmarkResponse], ResultWrapper[TimeTravelGetBookmarkResponse]),
        )

    async def restore(
        self,
        database_id: str,
        *,
        account_id: str,
        bookmark: str | Omit = omit,
        timestamp: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeTravelRestoreResponse:
        """
        Restores a D1 database to a previous point in time either via a bookmark or a
        timestamp.

        Args:
          account_id: Account identifier tag.

          database_id: D1 database identifier (UUID).

          bookmark: A bookmark to restore the database to. Required if `timestamp` is not provided.

          timestamp: An ISO 8601 timestamp to restore the database to. Required if `bookmark` is not
              provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not database_id:
            raise ValueError(f"Expected a non-empty value for `database_id` but received {database_id!r}")
        return await self._post(
            f"/accounts/{account_id}/d1/database/{database_id}/time_travel/restore",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "bookmark": bookmark,
                        "timestamp": timestamp,
                    },
                    time_travel_restore_params.TimeTravelRestoreParams,
                ),
                post_parser=ResultWrapper[TimeTravelRestoreResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeTravelRestoreResponse], ResultWrapper[TimeTravelRestoreResponse]),
        )


class TimeTravelResourceWithRawResponse:
    def __init__(self, time_travel: TimeTravelResource) -> None:
        self._time_travel = time_travel

        self.get_bookmark = to_raw_response_wrapper(
            time_travel.get_bookmark,
        )
        self.restore = to_raw_response_wrapper(
            time_travel.restore,
        )


class AsyncTimeTravelResourceWithRawResponse:
    def __init__(self, time_travel: AsyncTimeTravelResource) -> None:
        self._time_travel = time_travel

        self.get_bookmark = async_to_raw_response_wrapper(
            time_travel.get_bookmark,
        )
        self.restore = async_to_raw_response_wrapper(
            time_travel.restore,
        )


class TimeTravelResourceWithStreamingResponse:
    def __init__(self, time_travel: TimeTravelResource) -> None:
        self._time_travel = time_travel

        self.get_bookmark = to_streamed_response_wrapper(
            time_travel.get_bookmark,
        )
        self.restore = to_streamed_response_wrapper(
            time_travel.restore,
        )


class AsyncTimeTravelResourceWithStreamingResponse:
    def __init__(self, time_travel: AsyncTimeTravelResource) -> None:
        self._time_travel = time_travel

        self.get_bookmark = async_to_streamed_response_wrapper(
            time_travel.get_bookmark,
        )
        self.restore = async_to_streamed_response_wrapper(
            time_travel.restore,
        )
