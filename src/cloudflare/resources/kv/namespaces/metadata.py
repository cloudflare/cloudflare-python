# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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

__all__ = ["Metadata", "AsyncMetadata"]


class Metadata(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetadataWithRawResponse:
        return MetadataWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetadataWithStreamingResponse:
        return MetadataWithStreamingResponse(self)

    def get(
        self,
        key_name: str,
        *,
        account_id: str,
        namespace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Returns the metadata associated with the given key in the given namespace.

        Use
        URL-encoding to use special characters (for example, `:`, `!`, `%`) in the key
        name.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

          key_name: A key's name. The name may be at most 512 bytes. All printable, non-whitespace
              characters are valid. Use percent-encoding to define key names as part of a URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        if not key_name:
            raise ValueError(f"Expected a non-empty value for `key_name` but received {key_name!r}")
        return self._get(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/metadata/{key_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class AsyncMetadata(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetadataWithRawResponse:
        return AsyncMetadataWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetadataWithStreamingResponse:
        return AsyncMetadataWithStreamingResponse(self)

    async def get(
        self,
        key_name: str,
        *,
        account_id: str,
        namespace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Returns the metadata associated with the given key in the given namespace.

        Use
        URL-encoding to use special characters (for example, `:`, `!`, `%`) in the key
        name.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

          key_name: A key's name. The name may be at most 512 bytes. All printable, non-whitespace
              characters are valid. Use percent-encoding to define key names as part of a URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        if not key_name:
            raise ValueError(f"Expected a non-empty value for `key_name` but received {key_name!r}")
        return await self._get(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/metadata/{key_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class MetadataWithRawResponse:
    def __init__(self, metadata: Metadata) -> None:
        self._metadata = metadata

        self.get = to_raw_response_wrapper(
            metadata.get,
        )


class AsyncMetadataWithRawResponse:
    def __init__(self, metadata: AsyncMetadata) -> None:
        self._metadata = metadata

        self.get = async_to_raw_response_wrapper(
            metadata.get,
        )


class MetadataWithStreamingResponse:
    def __init__(self, metadata: Metadata) -> None:
        self._metadata = metadata

        self.get = to_streamed_response_wrapper(
            metadata.get,
        )


class AsyncMetadataWithStreamingResponse:
    def __init__(self, metadata: AsyncMetadata) -> None:
        self._metadata = metadata

        self.get = async_to_streamed_response_wrapper(
            metadata.get,
        )
