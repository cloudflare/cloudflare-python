# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.access import (
    BookmarkUpdateResponse,
    BookmarkDeleteResponse,
    BookmarkAccessBookmarkApplicationsDeprecatedListBookmarkApplicationsResponse,
    BookmarkGetResponse,
)

from typing import Type, Optional

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
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Bookmarks", "AsyncBookmarks"]


class Bookmarks(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BookmarksWithRawResponse:
        return BookmarksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BookmarksWithStreamingResponse:
        return BookmarksWithStreamingResponse(self)

    def update(
        self,
        uuid: str,
        *,
        identifier: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BookmarkUpdateResponse:
        """
        Updates a configured Bookmark application.

        Args:
          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._put(
            f"/accounts/{identifier}/access/bookmarks/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[BookmarkUpdateResponse], ResultWrapper[BookmarkUpdateResponse]),
        )

    def delete(
        self,
        uuid: str,
        *,
        identifier: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BookmarkDeleteResponse:
        """
        Deletes a Bookmark application.

        Args:
          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._delete(
            f"/accounts/{identifier}/access/bookmarks/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[BookmarkDeleteResponse], ResultWrapper[BookmarkDeleteResponse]),
        )

    def access_bookmark_applications_deprecated_list_bookmark_applications(
        self,
        identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BookmarkAccessBookmarkApplicationsDeprecatedListBookmarkApplicationsResponse]:
        """
        Lists Bookmark applications.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{identifier}/access/bookmarks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[BookmarkAccessBookmarkApplicationsDeprecatedListBookmarkApplicationsResponse]],
                ResultWrapper[BookmarkAccessBookmarkApplicationsDeprecatedListBookmarkApplicationsResponse],
            ),
        )

    def get(
        self,
        uuid: str,
        *,
        identifier: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BookmarkGetResponse:
        """
        Fetches a single Bookmark application.

        Args:
          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._get(
            f"/accounts/{identifier}/access/bookmarks/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[BookmarkGetResponse], ResultWrapper[BookmarkGetResponse]),
        )


class AsyncBookmarks(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBookmarksWithRawResponse:
        return AsyncBookmarksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBookmarksWithStreamingResponse:
        return AsyncBookmarksWithStreamingResponse(self)

    async def update(
        self,
        uuid: str,
        *,
        identifier: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BookmarkUpdateResponse:
        """
        Updates a configured Bookmark application.

        Args:
          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._put(
            f"/accounts/{identifier}/access/bookmarks/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[BookmarkUpdateResponse], ResultWrapper[BookmarkUpdateResponse]),
        )

    async def delete(
        self,
        uuid: str,
        *,
        identifier: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BookmarkDeleteResponse:
        """
        Deletes a Bookmark application.

        Args:
          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._delete(
            f"/accounts/{identifier}/access/bookmarks/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[BookmarkDeleteResponse], ResultWrapper[BookmarkDeleteResponse]),
        )

    async def access_bookmark_applications_deprecated_list_bookmark_applications(
        self,
        identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BookmarkAccessBookmarkApplicationsDeprecatedListBookmarkApplicationsResponse]:
        """
        Lists Bookmark applications.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{identifier}/access/bookmarks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[BookmarkAccessBookmarkApplicationsDeprecatedListBookmarkApplicationsResponse]],
                ResultWrapper[BookmarkAccessBookmarkApplicationsDeprecatedListBookmarkApplicationsResponse],
            ),
        )

    async def get(
        self,
        uuid: str,
        *,
        identifier: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BookmarkGetResponse:
        """
        Fetches a single Bookmark application.

        Args:
          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._get(
            f"/accounts/{identifier}/access/bookmarks/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[BookmarkGetResponse], ResultWrapper[BookmarkGetResponse]),
        )


class BookmarksWithRawResponse:
    def __init__(self, bookmarks: Bookmarks) -> None:
        self._bookmarks = bookmarks

        self.update = to_raw_response_wrapper(
            bookmarks.update,
        )
        self.delete = to_raw_response_wrapper(
            bookmarks.delete,
        )
        self.access_bookmark_applications_deprecated_list_bookmark_applications = to_raw_response_wrapper(
            bookmarks.access_bookmark_applications_deprecated_list_bookmark_applications,
        )
        self.get = to_raw_response_wrapper(
            bookmarks.get,
        )


class AsyncBookmarksWithRawResponse:
    def __init__(self, bookmarks: AsyncBookmarks) -> None:
        self._bookmarks = bookmarks

        self.update = async_to_raw_response_wrapper(
            bookmarks.update,
        )
        self.delete = async_to_raw_response_wrapper(
            bookmarks.delete,
        )
        self.access_bookmark_applications_deprecated_list_bookmark_applications = async_to_raw_response_wrapper(
            bookmarks.access_bookmark_applications_deprecated_list_bookmark_applications,
        )
        self.get = async_to_raw_response_wrapper(
            bookmarks.get,
        )


class BookmarksWithStreamingResponse:
    def __init__(self, bookmarks: Bookmarks) -> None:
        self._bookmarks = bookmarks

        self.update = to_streamed_response_wrapper(
            bookmarks.update,
        )
        self.delete = to_streamed_response_wrapper(
            bookmarks.delete,
        )
        self.access_bookmark_applications_deprecated_list_bookmark_applications = to_streamed_response_wrapper(
            bookmarks.access_bookmark_applications_deprecated_list_bookmark_applications,
        )
        self.get = to_streamed_response_wrapper(
            bookmarks.get,
        )


class AsyncBookmarksWithStreamingResponse:
    def __init__(self, bookmarks: AsyncBookmarks) -> None:
        self._bookmarks = bookmarks

        self.update = async_to_streamed_response_wrapper(
            bookmarks.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            bookmarks.delete,
        )
        self.access_bookmark_applications_deprecated_list_bookmark_applications = async_to_streamed_response_wrapper(
            bookmarks.access_bookmark_applications_deprecated_list_bookmark_applications,
        )
        self.get = async_to_streamed_response_wrapper(
            bookmarks.get,
        )
