# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast
from typing_extensions import Literal

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
from ...._base_client import make_request_options
from ....types.workers.assets import upload_create_params
from ....types.workers.assets.upload_create_response import UploadCreateResponse

__all__ = ["UploadResource", "AsyncUploadResource"]


class UploadResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UploadResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return UploadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UploadResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return UploadResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        base64: Literal[True],
        any_file_hash: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UploadCreateResponse]:
        """Upload assets ahead of creating a Worker version.

        To learn more about the direct
        uploads of assets, see
        https://developers.cloudflare.com/workers/static-assets/direct-upload/

        Args:
          account_id: Identifier

          base64: Whether the file contents are base64-encoded. Must be `true`.

          any_file_hash: Base-64 encoded contents of the file. The content type of the file should be
              included to ensure a valid "Content-Type" header is included in asset responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/accounts/{account_id}/workers/assets/upload",
            body=maybe_transform({"any_file_hash": any_file_hash}, upload_create_params.UploadCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"base64": base64}, upload_create_params.UploadCreateParams),
                post_parser=ResultWrapper[Optional[UploadCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UploadCreateResponse]], ResultWrapper[UploadCreateResponse]),
        )


class AsyncUploadResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUploadResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUploadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUploadResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncUploadResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        base64: Literal[True],
        any_file_hash: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UploadCreateResponse]:
        """Upload assets ahead of creating a Worker version.

        To learn more about the direct
        uploads of assets, see
        https://developers.cloudflare.com/workers/static-assets/direct-upload/

        Args:
          account_id: Identifier

          base64: Whether the file contents are base64-encoded. Must be `true`.

          any_file_hash: Base-64 encoded contents of the file. The content type of the file should be
              included to ensure a valid "Content-Type" header is included in asset responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/accounts/{account_id}/workers/assets/upload",
            body=await async_maybe_transform({"any_file_hash": any_file_hash}, upload_create_params.UploadCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"base64": base64}, upload_create_params.UploadCreateParams),
                post_parser=ResultWrapper[Optional[UploadCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UploadCreateResponse]], ResultWrapper[UploadCreateResponse]),
        )


class UploadResourceWithRawResponse:
    def __init__(self, upload: UploadResource) -> None:
        self._upload = upload

        self.create = to_raw_response_wrapper(
            upload.create,
        )


class AsyncUploadResourceWithRawResponse:
    def __init__(self, upload: AsyncUploadResource) -> None:
        self._upload = upload

        self.create = async_to_raw_response_wrapper(
            upload.create,
        )


class UploadResourceWithStreamingResponse:
    def __init__(self, upload: UploadResource) -> None:
        self._upload = upload

        self.create = to_streamed_response_wrapper(
            upload.create,
        )


class AsyncUploadResourceWithStreamingResponse:
    def __init__(self, upload: AsyncUploadResource) -> None:
        self._upload = upload

        self.create = async_to_streamed_response_wrapper(
            upload.create,
        )
