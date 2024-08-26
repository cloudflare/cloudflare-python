# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.kv.namespaces.metadata_get_response import MetadataGetResponse

from ...._wrappers import ResultWrapper

from typing import Optional, Type

from ...._base_client import make_request_options

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from typing import cast
from typing import cast

__all__ = ["MetadataResource", "AsyncMetadataResource"]

class MetadataResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetadataResourceWithRawResponse:
        return MetadataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetadataResourceWithStreamingResponse:
        return MetadataResourceWithStreamingResponse(self)

    def get(self,
    key_name: str,
    *,
    account_id: str,
    namespace_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[MetadataGetResponse]:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not namespace_id:
          raise ValueError(
            f'Expected a non-empty value for `namespace_id` but received {namespace_id!r}'
          )
        if not key_name:
          raise ValueError(
            f'Expected a non-empty value for `key_name` but received {key_name!r}'
          )
        return self._get(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/metadata/{key_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[MetadataGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[MetadataGetResponse]], ResultWrapper[MetadataGetResponse]),
        )

class AsyncMetadataResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetadataResourceWithRawResponse:
        return AsyncMetadataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetadataResourceWithStreamingResponse:
        return AsyncMetadataResourceWithStreamingResponse(self)

    async def get(self,
    key_name: str,
    *,
    account_id: str,
    namespace_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[MetadataGetResponse]:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not namespace_id:
          raise ValueError(
            f'Expected a non-empty value for `namespace_id` but received {namespace_id!r}'
          )
        if not key_name:
          raise ValueError(
            f'Expected a non-empty value for `key_name` but received {key_name!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/metadata/{key_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[MetadataGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[MetadataGetResponse]], ResultWrapper[MetadataGetResponse]),
        )

class MetadataResourceWithRawResponse:
    def __init__(self, metadata: MetadataResource) -> None:
        self._metadata = metadata

        self.get = to_raw_response_wrapper(
            metadata.get,
        )

class AsyncMetadataResourceWithRawResponse:
    def __init__(self, metadata: AsyncMetadataResource) -> None:
        self._metadata = metadata

        self.get = async_to_raw_response_wrapper(
            metadata.get,
        )

class MetadataResourceWithStreamingResponse:
    def __init__(self, metadata: MetadataResource) -> None:
        self._metadata = metadata

        self.get = to_streamed_response_wrapper(
            metadata.get,
        )

class AsyncMetadataResourceWithStreamingResponse:
    def __init__(self, metadata: AsyncMetadataResource) -> None:
        self._metadata = metadata

        self.get = async_to_streamed_response_wrapper(
            metadata.get,
        )