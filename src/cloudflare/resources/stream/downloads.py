# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

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
from ..._base_client import (
    make_request_options,
)
from ...types.shared import (
    UnnamedSchemaRef602dd5f63eab958d53da61434dec08f0,
    UnnamedSchemaRef9444735ca60712dbcf8afd832eb5716a,
)
from ...types.stream import download_create_params

__all__ = ["Downloads", "AsyncDownloads"]


class Downloads(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DownloadsWithRawResponse:
        return DownloadsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DownloadsWithStreamingResponse:
        return DownloadsWithStreamingResponse(self)

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
    ) -> UnnamedSchemaRef9444735ca60712dbcf8afd832eb5716a:
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
            UnnamedSchemaRef9444735ca60712dbcf8afd832eb5716a,
            self._post(
                f"/accounts/{account_id}/stream/{identifier}/downloads",
                body=maybe_transform(body, download_create_params.DownloadCreateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UnnamedSchemaRef9444735ca60712dbcf8afd832eb5716a]
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
    ) -> UnnamedSchemaRef602dd5f63eab958d53da61434dec08f0:
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
            UnnamedSchemaRef602dd5f63eab958d53da61434dec08f0,
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
                    Any, ResultWrapper[UnnamedSchemaRef602dd5f63eab958d53da61434dec08f0]
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
    ) -> UnnamedSchemaRef9444735ca60712dbcf8afd832eb5716a:
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
            UnnamedSchemaRef9444735ca60712dbcf8afd832eb5716a,
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
                    Any, ResultWrapper[UnnamedSchemaRef9444735ca60712dbcf8afd832eb5716a]
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
    ) -> UnnamedSchemaRef9444735ca60712dbcf8afd832eb5716a:
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
            UnnamedSchemaRef9444735ca60712dbcf8afd832eb5716a,
            await self._post(
                f"/accounts/{account_id}/stream/{identifier}/downloads",
                body=await async_maybe_transform(body, download_create_params.DownloadCreateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UnnamedSchemaRef9444735ca60712dbcf8afd832eb5716a]
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
    ) -> UnnamedSchemaRef602dd5f63eab958d53da61434dec08f0:
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
            UnnamedSchemaRef602dd5f63eab958d53da61434dec08f0,
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
                    Any, ResultWrapper[UnnamedSchemaRef602dd5f63eab958d53da61434dec08f0]
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
    ) -> UnnamedSchemaRef9444735ca60712dbcf8afd832eb5716a:
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
            UnnamedSchemaRef9444735ca60712dbcf8afd832eb5716a,
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
                    Any, ResultWrapper[UnnamedSchemaRef9444735ca60712dbcf8afd832eb5716a]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class DownloadsWithRawResponse:
    def __init__(self, downloads: Downloads) -> None:
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


class AsyncDownloadsWithRawResponse:
    def __init__(self, downloads: AsyncDownloads) -> None:
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


class DownloadsWithStreamingResponse:
    def __init__(self, downloads: Downloads) -> None:
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


class AsyncDownloadsWithStreamingResponse:
    def __init__(self, downloads: AsyncDownloads) -> None:
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
