# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.stream import (
    DownloadDeleteResponse,
    DownloadStreamMP4DownloadsCreateDownloadsResponse,
    DownloadStreamMP4DownloadsListDownloadsResponse,
)

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
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Downloads", "AsyncDownloads"]


class Downloads(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DownloadsWithRawResponse:
        return DownloadsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DownloadsWithStreamingResponse:
        return DownloadsWithStreamingResponse(self)

    def delete(
        self,
        identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DownloadDeleteResponse:
        """
        Delete the downloads for a video.

        Args:
          account_id: Identifier

          identifier: A Cloudflare-generated unique identifier for a media item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            DownloadDeleteResponse,
            self._delete(
                f"/accounts/{account_id}/stream/{identifier}/downloads",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DownloadDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def stream_m_p_4_downloads_create_downloads(
        self,
        identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DownloadStreamMP4DownloadsCreateDownloadsResponse:
        """
        Creates a download for a video when a video is ready to view.

        Args:
          account_id: Identifier

          identifier: A Cloudflare-generated unique identifier for a media item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            DownloadStreamMP4DownloadsCreateDownloadsResponse,
            self._post(
                f"/accounts/{account_id}/stream/{identifier}/downloads",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DownloadStreamMP4DownloadsCreateDownloadsResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def stream_m_p_4_downloads_list_downloads(
        self,
        identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DownloadStreamMP4DownloadsListDownloadsResponse:
        """
        Lists the downloads created for a video.

        Args:
          account_id: Identifier

          identifier: A Cloudflare-generated unique identifier for a media item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            DownloadStreamMP4DownloadsListDownloadsResponse,
            self._get(
                f"/accounts/{account_id}/stream/{identifier}/downloads",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DownloadStreamMP4DownloadsListDownloadsResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncDownloads(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDownloadsWithRawResponse:
        return AsyncDownloadsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDownloadsWithStreamingResponse:
        return AsyncDownloadsWithStreamingResponse(self)

    async def delete(
        self,
        identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DownloadDeleteResponse:
        """
        Delete the downloads for a video.

        Args:
          account_id: Identifier

          identifier: A Cloudflare-generated unique identifier for a media item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            DownloadDeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/stream/{identifier}/downloads",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DownloadDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def stream_m_p_4_downloads_create_downloads(
        self,
        identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DownloadStreamMP4DownloadsCreateDownloadsResponse:
        """
        Creates a download for a video when a video is ready to view.

        Args:
          account_id: Identifier

          identifier: A Cloudflare-generated unique identifier for a media item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            DownloadStreamMP4DownloadsCreateDownloadsResponse,
            await self._post(
                f"/accounts/{account_id}/stream/{identifier}/downloads",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DownloadStreamMP4DownloadsCreateDownloadsResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def stream_m_p_4_downloads_list_downloads(
        self,
        identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DownloadStreamMP4DownloadsListDownloadsResponse:
        """
        Lists the downloads created for a video.

        Args:
          account_id: Identifier

          identifier: A Cloudflare-generated unique identifier for a media item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            DownloadStreamMP4DownloadsListDownloadsResponse,
            await self._get(
                f"/accounts/{account_id}/stream/{identifier}/downloads",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DownloadStreamMP4DownloadsListDownloadsResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class DownloadsWithRawResponse:
    def __init__(self, downloads: Downloads) -> None:
        self._downloads = downloads

        self.delete = to_raw_response_wrapper(
            downloads.delete,
        )
        self.stream_m_p_4_downloads_create_downloads = to_raw_response_wrapper(
            downloads.stream_m_p_4_downloads_create_downloads,
        )
        self.stream_m_p_4_downloads_list_downloads = to_raw_response_wrapper(
            downloads.stream_m_p_4_downloads_list_downloads,
        )


class AsyncDownloadsWithRawResponse:
    def __init__(self, downloads: AsyncDownloads) -> None:
        self._downloads = downloads

        self.delete = async_to_raw_response_wrapper(
            downloads.delete,
        )
        self.stream_m_p_4_downloads_create_downloads = async_to_raw_response_wrapper(
            downloads.stream_m_p_4_downloads_create_downloads,
        )
        self.stream_m_p_4_downloads_list_downloads = async_to_raw_response_wrapper(
            downloads.stream_m_p_4_downloads_list_downloads,
        )


class DownloadsWithStreamingResponse:
    def __init__(self, downloads: Downloads) -> None:
        self._downloads = downloads

        self.delete = to_streamed_response_wrapper(
            downloads.delete,
        )
        self.stream_m_p_4_downloads_create_downloads = to_streamed_response_wrapper(
            downloads.stream_m_p_4_downloads_create_downloads,
        )
        self.stream_m_p_4_downloads_list_downloads = to_streamed_response_wrapper(
            downloads.stream_m_p_4_downloads_list_downloads,
        )


class AsyncDownloadsWithStreamingResponse:
    def __init__(self, downloads: AsyncDownloads) -> None:
        self._downloads = downloads

        self.delete = async_to_streamed_response_wrapper(
            downloads.delete,
        )
        self.stream_m_p_4_downloads_create_downloads = async_to_streamed_response_wrapper(
            downloads.stream_m_p_4_downloads_create_downloads,
        )
        self.stream_m_p_4_downloads_list_downloads = async_to_streamed_response_wrapper(
            downloads.stream_m_p_4_downloads_list_downloads,
        )
