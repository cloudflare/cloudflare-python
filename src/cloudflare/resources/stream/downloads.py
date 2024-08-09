# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import make_request_options
from ...types.stream import download_create_params
from ...types.stream.download_get_response import DownloadGetResponse
from ...types.stream.download_create_response import DownloadCreateResponse
from ...types.stream.download_delete_response import DownloadDeleteResponse

__all__ = ["DownloadsResource", "AsyncDownloadsResource"]


class DownloadsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DownloadsResourceWithRawResponse:
        return DownloadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DownloadsResourceWithStreamingResponse:
        return DownloadsResourceWithStreamingResponse(self)

    def create(
        self,
        identifier: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DownloadCreateResponse]:
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
            Optional[DownloadCreateResponse],
            self._post(
                f"/accounts/{account_id}/stream/{identifier}/downloads",
                body=maybe_transform(body, download_create_params.DownloadCreateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[DownloadCreateResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DownloadCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

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
    ) -> Optional[DownloadDeleteResponse]:
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
            Optional[DownloadDeleteResponse],
            self._delete(
                f"/accounts/{account_id}/stream/{identifier}/downloads",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[DownloadDeleteResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DownloadDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
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
    ) -> Optional[DownloadGetResponse]:
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
            Optional[DownloadGetResponse],
            self._get(
                f"/accounts/{account_id}/stream/{identifier}/downloads",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[DownloadGetResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DownloadGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncDownloadsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDownloadsResourceWithRawResponse:
        return AsyncDownloadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDownloadsResourceWithStreamingResponse:
        return AsyncDownloadsResourceWithStreamingResponse(self)

    async def create(
        self,
        identifier: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DownloadCreateResponse]:
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
            Optional[DownloadCreateResponse],
            await self._post(
                f"/accounts/{account_id}/stream/{identifier}/downloads",
                body=await async_maybe_transform(body, download_create_params.DownloadCreateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[DownloadCreateResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DownloadCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

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
    ) -> Optional[DownloadDeleteResponse]:
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
            Optional[DownloadDeleteResponse],
            await self._delete(
                f"/accounts/{account_id}/stream/{identifier}/downloads",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[DownloadDeleteResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DownloadDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
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
    ) -> Optional[DownloadGetResponse]:
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
            Optional[DownloadGetResponse],
            await self._get(
                f"/accounts/{account_id}/stream/{identifier}/downloads",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[DownloadGetResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DownloadGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class DownloadsResourceWithRawResponse:
    def __init__(self, downloads: DownloadsResource) -> None:
        self._downloads = downloads

        self.create = to_raw_response_wrapper(
            downloads.create,
        )
        self.delete = to_raw_response_wrapper(
            downloads.delete,
        )
        self.get = to_raw_response_wrapper(
            downloads.get,
        )


class AsyncDownloadsResourceWithRawResponse:
    def __init__(self, downloads: AsyncDownloadsResource) -> None:
        self._downloads = downloads

        self.create = async_to_raw_response_wrapper(
            downloads.create,
        )
        self.delete = async_to_raw_response_wrapper(
            downloads.delete,
        )
        self.get = async_to_raw_response_wrapper(
            downloads.get,
        )


class DownloadsResourceWithStreamingResponse:
    def __init__(self, downloads: DownloadsResource) -> None:
        self._downloads = downloads

        self.create = to_streamed_response_wrapper(
            downloads.create,
        )
        self.delete = to_streamed_response_wrapper(
            downloads.delete,
        )
        self.get = to_streamed_response_wrapper(
            downloads.get,
        )


class AsyncDownloadsResourceWithStreamingResponse:
    def __init__(self, downloads: AsyncDownloadsResource) -> None:
        self._downloads = downloads

        self.create = async_to_streamed_response_wrapper(
            downloads.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            downloads.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            downloads.get,
        )
