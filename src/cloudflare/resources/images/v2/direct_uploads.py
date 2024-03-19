# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, cast
from datetime import datetime

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.images.v2 import DirectUploadCreateResponse, direct_upload_create_params

__all__ = ["DirectUploads", "AsyncDirectUploads"]


class DirectUploads(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DirectUploadsWithRawResponse:
        return DirectUploadsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DirectUploadsWithStreamingResponse:
        return DirectUploadsWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        expiry: Union[str, datetime] | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        require_signed_urls: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DirectUploadCreateResponse:
        """Direct uploads allow users to upload images without API keys.

        A common use case
        are web apps, client-side applications, or mobile devices where users upload
        content directly to Cloudflare Images. This method creates a draft record for a
        future image. It returns an upload URL and an image identifier. To verify if the
        image itself has been uploaded, send an image details request
        (accounts/:account_identifier/images/v1/:identifier), and check that the
        `draft: true` property is not present.

        Args:
          account_id: Account identifier tag.

          expiry: The date after which the upload will not be accepted. Minimum: Now + 2 minutes.
              Maximum: Now + 6 hours.

          metadata: User modifiable key-value store. Can be used for keeping references to another
              system of record, for managing images.

          require_signed_urls: Indicates whether the image requires a signature token to be accessed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/images/v2/direct_upload",
            body=maybe_transform(
                {
                    "expiry": expiry,
                    "metadata": metadata,
                    "require_signed_urls": require_signed_urls,
                },
                direct_upload_create_params.DirectUploadCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DirectUploadCreateResponse], ResultWrapper[DirectUploadCreateResponse]),
        )


class AsyncDirectUploads(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDirectUploadsWithRawResponse:
        return AsyncDirectUploadsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDirectUploadsWithStreamingResponse:
        return AsyncDirectUploadsWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        expiry: Union[str, datetime] | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        require_signed_urls: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DirectUploadCreateResponse:
        """Direct uploads allow users to upload images without API keys.

        A common use case
        are web apps, client-side applications, or mobile devices where users upload
        content directly to Cloudflare Images. This method creates a draft record for a
        future image. It returns an upload URL and an image identifier. To verify if the
        image itself has been uploaded, send an image details request
        (accounts/:account_identifier/images/v1/:identifier), and check that the
        `draft: true` property is not present.

        Args:
          account_id: Account identifier tag.

          expiry: The date after which the upload will not be accepted. Minimum: Now + 2 minutes.
              Maximum: Now + 6 hours.

          metadata: User modifiable key-value store. Can be used for keeping references to another
              system of record, for managing images.

          require_signed_urls: Indicates whether the image requires a signature token to be accessed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/images/v2/direct_upload",
            body=await async_maybe_transform(
                {
                    "expiry": expiry,
                    "metadata": metadata,
                    "require_signed_urls": require_signed_urls,
                },
                direct_upload_create_params.DirectUploadCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DirectUploadCreateResponse], ResultWrapper[DirectUploadCreateResponse]),
        )


class DirectUploadsWithRawResponse:
    def __init__(self, direct_uploads: DirectUploads) -> None:
        self._direct_uploads = direct_uploads

        self.create = to_raw_response_wrapper(
            direct_uploads.create,
        )


class AsyncDirectUploadsWithRawResponse:
    def __init__(self, direct_uploads: AsyncDirectUploads) -> None:
        self._direct_uploads = direct_uploads

        self.create = async_to_raw_response_wrapper(
            direct_uploads.create,
        )


class DirectUploadsWithStreamingResponse:
    def __init__(self, direct_uploads: DirectUploads) -> None:
        self._direct_uploads = direct_uploads

        self.create = to_streamed_response_wrapper(
            direct_uploads.create,
        )


class AsyncDirectUploadsWithStreamingResponse:
    def __init__(self, direct_uploads: AsyncDirectUploads) -> None:
        self._direct_uploads = direct_uploads

        self.create = async_to_streamed_response_wrapper(
            direct_uploads.create,
        )
