# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Type, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.zero_trust.access import bookmark_create_params, bookmark_update_params
from ....types.zero_trust.access.bookmark import Bookmark
from ....types.zero_trust.access.bookmark_delete_response import BookmarkDeleteResponse

__all__ = ["BookmarksResource", "AsyncBookmarksResource"]


class BookmarksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BookmarksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return BookmarksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BookmarksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return BookmarksResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def create(
        self,
        bookmark_id: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Bookmark]:
        """
        Create a new Bookmark application.

        Args:
          bookmark_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bookmark_id:
            raise ValueError(f"Expected a non-empty value for `bookmark_id` but received {bookmark_id!r}")
        return self._post(
            f"/accounts/{account_id}/access/bookmarks/{bookmark_id}",
            body=maybe_transform(body, bookmark_create_params.BookmarkCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Bookmark]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Bookmark]], ResultWrapper[Bookmark]),
        )

    @typing_extensions.deprecated("deprecated")
    def update(
        self,
        bookmark_id: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Bookmark]:
        """
        Updates a configured Bookmark application.

        Args:
          bookmark_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bookmark_id:
            raise ValueError(f"Expected a non-empty value for `bookmark_id` but received {bookmark_id!r}")
        return self._put(
            f"/accounts/{account_id}/access/bookmarks/{bookmark_id}",
            body=maybe_transform(body, bookmark_update_params.BookmarkUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Bookmark]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Bookmark]], ResultWrapper[Bookmark]),
        )

    @typing_extensions.deprecated("deprecated")
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
    ) -> SyncSinglePage[Bookmark]:
        """
        Lists Bookmark applications.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/access/bookmarks",
            page=SyncSinglePage[Bookmark],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Bookmark,
        )

    @typing_extensions.deprecated("deprecated")
    def delete(
        self,
        bookmark_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BookmarkDeleteResponse]:
        """
        Deletes a Bookmark application.

        Args:
          bookmark_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bookmark_id:
            raise ValueError(f"Expected a non-empty value for `bookmark_id` but received {bookmark_id!r}")
        return self._delete(
            f"/accounts/{account_id}/access/bookmarks/{bookmark_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BookmarkDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BookmarkDeleteResponse]], ResultWrapper[BookmarkDeleteResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    def get(
        self,
        bookmark_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Bookmark]:
        """
        Fetches a single Bookmark application.

        Args:
          bookmark_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bookmark_id:
            raise ValueError(f"Expected a non-empty value for `bookmark_id` but received {bookmark_id!r}")
        return self._get(
            f"/accounts/{account_id}/access/bookmarks/{bookmark_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Bookmark]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Bookmark]], ResultWrapper[Bookmark]),
        )


class AsyncBookmarksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBookmarksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBookmarksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBookmarksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncBookmarksResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def create(
        self,
        bookmark_id: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Bookmark]:
        """
        Create a new Bookmark application.

        Args:
          bookmark_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bookmark_id:
            raise ValueError(f"Expected a non-empty value for `bookmark_id` but received {bookmark_id!r}")
        return await self._post(
            f"/accounts/{account_id}/access/bookmarks/{bookmark_id}",
            body=await async_maybe_transform(body, bookmark_create_params.BookmarkCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Bookmark]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Bookmark]], ResultWrapper[Bookmark]),
        )

    @typing_extensions.deprecated("deprecated")
    async def update(
        self,
        bookmark_id: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Bookmark]:
        """
        Updates a configured Bookmark application.

        Args:
          bookmark_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bookmark_id:
            raise ValueError(f"Expected a non-empty value for `bookmark_id` but received {bookmark_id!r}")
        return await self._put(
            f"/accounts/{account_id}/access/bookmarks/{bookmark_id}",
            body=await async_maybe_transform(body, bookmark_update_params.BookmarkUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Bookmark]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Bookmark]], ResultWrapper[Bookmark]),
        )

    @typing_extensions.deprecated("deprecated")
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
    ) -> AsyncPaginator[Bookmark, AsyncSinglePage[Bookmark]]:
        """
        Lists Bookmark applications.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/access/bookmarks",
            page=AsyncSinglePage[Bookmark],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Bookmark,
        )

    @typing_extensions.deprecated("deprecated")
    async def delete(
        self,
        bookmark_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BookmarkDeleteResponse]:
        """
        Deletes a Bookmark application.

        Args:
          bookmark_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bookmark_id:
            raise ValueError(f"Expected a non-empty value for `bookmark_id` but received {bookmark_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/access/bookmarks/{bookmark_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BookmarkDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BookmarkDeleteResponse]], ResultWrapper[BookmarkDeleteResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    async def get(
        self,
        bookmark_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Bookmark]:
        """
        Fetches a single Bookmark application.

        Args:
          bookmark_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bookmark_id:
            raise ValueError(f"Expected a non-empty value for `bookmark_id` but received {bookmark_id!r}")
        return await self._get(
            f"/accounts/{account_id}/access/bookmarks/{bookmark_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Bookmark]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Bookmark]], ResultWrapper[Bookmark]),
        )


class BookmarksResourceWithRawResponse:
    def __init__(self, bookmarks: BookmarksResource) -> None:
        self._bookmarks = bookmarks

        self.create = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                bookmarks.create  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                bookmarks.update  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                bookmarks.list  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                bookmarks.delete  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                bookmarks.get  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncBookmarksResourceWithRawResponse:
    def __init__(self, bookmarks: AsyncBookmarksResource) -> None:
        self._bookmarks = bookmarks

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                bookmarks.create  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                bookmarks.update  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                bookmarks.list  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                bookmarks.delete  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                bookmarks.get  # pyright: ignore[reportDeprecated],
            )
        )


class BookmarksResourceWithStreamingResponse:
    def __init__(self, bookmarks: BookmarksResource) -> None:
        self._bookmarks = bookmarks

        self.create = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                bookmarks.create  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                bookmarks.update  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                bookmarks.list  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                bookmarks.delete  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                bookmarks.get  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncBookmarksResourceWithStreamingResponse:
    def __init__(self, bookmarks: AsyncBookmarksResource) -> None:
        self._bookmarks = bookmarks

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                bookmarks.create  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                bookmarks.update  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                bookmarks.list  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                bookmarks.delete  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                bookmarks.get  # pyright: ignore[reportDeprecated],
            )
        )
