# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven, FileTypes
from ..._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.cloudforce_one import binary_storage_create_params
from ...types.cloudforce_one.binary_storage_create_response import BinaryStorageCreateResponse

__all__ = ["BinaryStorageResource", "AsyncBinaryStorageResource"]


class BinaryStorageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BinaryStorageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return BinaryStorageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BinaryStorageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return BinaryStorageResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryStorageCreateResponse:
        """
        Posts a file to Binary Storage

        Args:
          account_id: Account ID.

          file: The binary file content to upload.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/accounts/{account_id}/cloudforce-one/binary",
            body=maybe_transform(body, binary_storage_create_params.BinaryStorageCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryStorageCreateResponse,
        )

    def get(
        self,
        hash: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Retrieves a file from Binary Storage

        Args:
          account_id: Account ID.

          hash: hash of the binary

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not hash:
            raise ValueError(f"Expected a non-empty value for `hash` but received {hash!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/accounts/{account_id}/cloudforce-one/binary/{hash}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncBinaryStorageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBinaryStorageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBinaryStorageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBinaryStorageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncBinaryStorageResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryStorageCreateResponse:
        """
        Posts a file to Binary Storage

        Args:
          account_id: Account ID.

          file: The binary file content to upload.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/accounts/{account_id}/cloudforce-one/binary",
            body=await async_maybe_transform(body, binary_storage_create_params.BinaryStorageCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryStorageCreateResponse,
        )

    async def get(
        self,
        hash: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Retrieves a file from Binary Storage

        Args:
          account_id: Account ID.

          hash: hash of the binary

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not hash:
            raise ValueError(f"Expected a non-empty value for `hash` but received {hash!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/accounts/{account_id}/cloudforce-one/binary/{hash}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class BinaryStorageResourceWithRawResponse:
    def __init__(self, binary_storage: BinaryStorageResource) -> None:
        self._binary_storage = binary_storage

        self.create = to_raw_response_wrapper(
            binary_storage.create,
        )
        self.get = to_raw_response_wrapper(
            binary_storage.get,
        )


class AsyncBinaryStorageResourceWithRawResponse:
    def __init__(self, binary_storage: AsyncBinaryStorageResource) -> None:
        self._binary_storage = binary_storage

        self.create = async_to_raw_response_wrapper(
            binary_storage.create,
        )
        self.get = async_to_raw_response_wrapper(
            binary_storage.get,
        )


class BinaryStorageResourceWithStreamingResponse:
    def __init__(self, binary_storage: BinaryStorageResource) -> None:
        self._binary_storage = binary_storage

        self.create = to_streamed_response_wrapper(
            binary_storage.create,
        )
        self.get = to_streamed_response_wrapper(
            binary_storage.get,
        )


class AsyncBinaryStorageResourceWithStreamingResponse:
    def __init__(self, binary_storage: AsyncBinaryStorageResource) -> None:
        self._binary_storage = binary_storage

        self.create = async_to_streamed_response_wrapper(
            binary_storage.create,
        )
        self.get = async_to_streamed_response_wrapper(
            binary_storage.get,
        )
