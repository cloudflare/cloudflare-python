# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
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
from ....types.vectorize.indexes import metadata_index_create_params, metadata_index_delete_params
from ....types.vectorize.indexes.metadata_index_list_response import MetadataIndexListResponse
from ....types.vectorize.indexes.metadata_index_create_response import MetadataIndexCreateResponse
from ....types.vectorize.indexes.metadata_index_delete_response import MetadataIndexDeleteResponse

__all__ = ["MetadataIndexResource", "AsyncMetadataIndexResource"]


class MetadataIndexResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetadataIndexResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return MetadataIndexResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetadataIndexResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return MetadataIndexResourceWithStreamingResponse(self)

    def create(
        self,
        index_name: str,
        *,
        account_id: str,
        index_type: Literal["string", "number", "boolean"],
        property_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MetadataIndexCreateResponse]:
        """Enable metadata filtering based on metadata property.

        Limited to 10 properties.

        Args:
          account_id: Identifier

          index_type: Specifies the type of metadata property to index.

          property_name: Specifies the metadata property to index.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return self._post(
            f"/accounts/{account_id}/vectorize/v2/indexes/{index_name}/metadata_index/create",
            body=maybe_transform(
                {
                    "index_type": index_type,
                    "property_name": property_name,
                },
                metadata_index_create_params.MetadataIndexCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MetadataIndexCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MetadataIndexCreateResponse]], ResultWrapper[MetadataIndexCreateResponse]),
        )

    def list(
        self,
        index_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MetadataIndexListResponse]:
        """
        List Metadata Indexes for the specified Vectorize Index.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return self._get(
            f"/accounts/{account_id}/vectorize/v2/indexes/{index_name}/metadata_index/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MetadataIndexListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MetadataIndexListResponse]], ResultWrapper[MetadataIndexListResponse]),
        )

    def delete(
        self,
        index_name: str,
        *,
        account_id: str,
        property_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MetadataIndexDeleteResponse]:
        """
        Allow Vectorize to delete the specified metadata index.

        Args:
          account_id: Identifier

          property_name: Specifies the metadata property for which the index must be deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return self._post(
            f"/accounts/{account_id}/vectorize/v2/indexes/{index_name}/metadata_index/delete",
            body=maybe_transform(
                {"property_name": property_name}, metadata_index_delete_params.MetadataIndexDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MetadataIndexDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MetadataIndexDeleteResponse]], ResultWrapper[MetadataIndexDeleteResponse]),
        )


class AsyncMetadataIndexResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetadataIndexResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetadataIndexResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetadataIndexResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncMetadataIndexResourceWithStreamingResponse(self)

    async def create(
        self,
        index_name: str,
        *,
        account_id: str,
        index_type: Literal["string", "number", "boolean"],
        property_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MetadataIndexCreateResponse]:
        """Enable metadata filtering based on metadata property.

        Limited to 10 properties.

        Args:
          account_id: Identifier

          index_type: Specifies the type of metadata property to index.

          property_name: Specifies the metadata property to index.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return await self._post(
            f"/accounts/{account_id}/vectorize/v2/indexes/{index_name}/metadata_index/create",
            body=await async_maybe_transform(
                {
                    "index_type": index_type,
                    "property_name": property_name,
                },
                metadata_index_create_params.MetadataIndexCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MetadataIndexCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MetadataIndexCreateResponse]], ResultWrapper[MetadataIndexCreateResponse]),
        )

    async def list(
        self,
        index_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MetadataIndexListResponse]:
        """
        List Metadata Indexes for the specified Vectorize Index.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return await self._get(
            f"/accounts/{account_id}/vectorize/v2/indexes/{index_name}/metadata_index/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MetadataIndexListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MetadataIndexListResponse]], ResultWrapper[MetadataIndexListResponse]),
        )

    async def delete(
        self,
        index_name: str,
        *,
        account_id: str,
        property_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MetadataIndexDeleteResponse]:
        """
        Allow Vectorize to delete the specified metadata index.

        Args:
          account_id: Identifier

          property_name: Specifies the metadata property for which the index must be deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return await self._post(
            f"/accounts/{account_id}/vectorize/v2/indexes/{index_name}/metadata_index/delete",
            body=await async_maybe_transform(
                {"property_name": property_name}, metadata_index_delete_params.MetadataIndexDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MetadataIndexDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MetadataIndexDeleteResponse]], ResultWrapper[MetadataIndexDeleteResponse]),
        )


class MetadataIndexResourceWithRawResponse:
    def __init__(self, metadata_index: MetadataIndexResource) -> None:
        self._metadata_index = metadata_index

        self.create = to_raw_response_wrapper(
            metadata_index.create,
        )
        self.list = to_raw_response_wrapper(
            metadata_index.list,
        )
        self.delete = to_raw_response_wrapper(
            metadata_index.delete,
        )


class AsyncMetadataIndexResourceWithRawResponse:
    def __init__(self, metadata_index: AsyncMetadataIndexResource) -> None:
        self._metadata_index = metadata_index

        self.create = async_to_raw_response_wrapper(
            metadata_index.create,
        )
        self.list = async_to_raw_response_wrapper(
            metadata_index.list,
        )
        self.delete = async_to_raw_response_wrapper(
            metadata_index.delete,
        )


class MetadataIndexResourceWithStreamingResponse:
    def __init__(self, metadata_index: MetadataIndexResource) -> None:
        self._metadata_index = metadata_index

        self.create = to_streamed_response_wrapper(
            metadata_index.create,
        )
        self.list = to_streamed_response_wrapper(
            metadata_index.list,
        )
        self.delete = to_streamed_response_wrapper(
            metadata_index.delete,
        )


class AsyncMetadataIndexResourceWithStreamingResponse:
    def __init__(self, metadata_index: AsyncMetadataIndexResource) -> None:
        self._metadata_index = metadata_index

        self.create = async_to_streamed_response_wrapper(
            metadata_index.create,
        )
        self.list = async_to_streamed_response_wrapper(
            metadata_index.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            metadata_index.delete,
        )
