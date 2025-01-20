# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...._base_client import make_request_options

__all__ = ["BlobsResource", "AsyncBlobsResource"]


class BlobsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BlobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return BlobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BlobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return BlobsResourceWithStreamingResponse(self)

    def get(
        self,
        image_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """Fetch base image.

        For most images this will be the originally uploaded file. For
        larger images it can be a near-lossless version of the original.

        Args:
          account_id: Account identifier tag.

          image_id: Image unique identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        extra_headers = {"Accept": "image/*", **(extra_headers or {})}
        return self._get(
            f"/accounts/{account_id}/images/v1/{image_id}/blob",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncBlobsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBlobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBlobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBlobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncBlobsResourceWithStreamingResponse(self)

    async def get(
        self,
        image_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """Fetch base image.

        For most images this will be the originally uploaded file. For
        larger images it can be a near-lossless version of the original.

        Args:
          account_id: Account identifier tag.

          image_id: Image unique identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        extra_headers = {"Accept": "image/*", **(extra_headers or {})}
        return await self._get(
            f"/accounts/{account_id}/images/v1/{image_id}/blob",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class BlobsResourceWithRawResponse:
    def __init__(self, blobs: BlobsResource) -> None:
        self._blobs = blobs

        self.get = to_custom_raw_response_wrapper(
            blobs.get,
            BinaryAPIResponse,
        )


class AsyncBlobsResourceWithRawResponse:
    def __init__(self, blobs: AsyncBlobsResource) -> None:
        self._blobs = blobs

        self.get = async_to_custom_raw_response_wrapper(
            blobs.get,
            AsyncBinaryAPIResponse,
        )


class BlobsResourceWithStreamingResponse:
    def __init__(self, blobs: BlobsResource) -> None:
        self._blobs = blobs

        self.get = to_custom_streamed_response_wrapper(
            blobs.get,
            StreamedBinaryAPIResponse,
        )


class AsyncBlobsResourceWithStreamingResponse:
    def __init__(self, blobs: AsyncBlobsResource) -> None:
        self._blobs = blobs

        self.get = async_to_custom_streamed_response_wrapper(
            blobs.get,
            AsyncStreamedBinaryAPIResponse,
        )
