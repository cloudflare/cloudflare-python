# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types import (
    ManagedHeaderListResponse,
    ManagedHeaderManagedTransformsUpdateStatusOfManagedTransformsResponse,
    managed_header_managed_transforms_update_status_of_managed_transforms_params,
)

from typing import Iterable

from .._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ..types import shared_params
from ..types import managed_header_managed_transforms_update_status_of_managed_transforms_params
from .._wrappers import ResultWrapper

__all__ = ["ManagedHeaders", "AsyncManagedHeaders"]


class ManagedHeaders(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ManagedHeadersWithRawResponse:
        return ManagedHeadersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ManagedHeadersWithStreamingResponse:
        return ManagedHeadersWithStreamingResponse(self)

    def list(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ManagedHeaderListResponse:
        """
        Fetches a list of all Managed Transforms.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/managed_headers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagedHeaderListResponse,
        )

    def managed_transforms_update_status_of_managed_transforms(
        self,
        zone_id: str,
        *,
        managed_request_headers: Iterable[
            managed_header_managed_transforms_update_status_of_managed_transforms_params.ManagedRequestHeader
        ],
        managed_response_headers: Iterable[
            managed_header_managed_transforms_update_status_of_managed_transforms_params.ManagedResponseHeader
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ManagedHeaderManagedTransformsUpdateStatusOfManagedTransformsResponse:
        """
        Updates the status of one or more Managed Transforms.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/managed_headers",
            body=maybe_transform(
                {
                    "managed_request_headers": managed_request_headers,
                    "managed_response_headers": managed_response_headers,
                },
                managed_header_managed_transforms_update_status_of_managed_transforms_params.ManagedHeaderManagedTransformsUpdateStatusOfManagedTransformsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagedHeaderManagedTransformsUpdateStatusOfManagedTransformsResponse,
        )


class AsyncManagedHeaders(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncManagedHeadersWithRawResponse:
        return AsyncManagedHeadersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncManagedHeadersWithStreamingResponse:
        return AsyncManagedHeadersWithStreamingResponse(self)

    async def list(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ManagedHeaderListResponse:
        """
        Fetches a list of all Managed Transforms.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/managed_headers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagedHeaderListResponse,
        )

    async def managed_transforms_update_status_of_managed_transforms(
        self,
        zone_id: str,
        *,
        managed_request_headers: Iterable[
            managed_header_managed_transforms_update_status_of_managed_transforms_params.ManagedRequestHeader
        ],
        managed_response_headers: Iterable[
            managed_header_managed_transforms_update_status_of_managed_transforms_params.ManagedResponseHeader
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ManagedHeaderManagedTransformsUpdateStatusOfManagedTransformsResponse:
        """
        Updates the status of one or more Managed Transforms.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/managed_headers",
            body=maybe_transform(
                {
                    "managed_request_headers": managed_request_headers,
                    "managed_response_headers": managed_response_headers,
                },
                managed_header_managed_transforms_update_status_of_managed_transforms_params.ManagedHeaderManagedTransformsUpdateStatusOfManagedTransformsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagedHeaderManagedTransformsUpdateStatusOfManagedTransformsResponse,
        )


class ManagedHeadersWithRawResponse:
    def __init__(self, managed_headers: ManagedHeaders) -> None:
        self._managed_headers = managed_headers

        self.list = to_raw_response_wrapper(
            managed_headers.list,
        )
        self.managed_transforms_update_status_of_managed_transforms = to_raw_response_wrapper(
            managed_headers.managed_transforms_update_status_of_managed_transforms,
        )


class AsyncManagedHeadersWithRawResponse:
    def __init__(self, managed_headers: AsyncManagedHeaders) -> None:
        self._managed_headers = managed_headers

        self.list = async_to_raw_response_wrapper(
            managed_headers.list,
        )
        self.managed_transforms_update_status_of_managed_transforms = async_to_raw_response_wrapper(
            managed_headers.managed_transforms_update_status_of_managed_transforms,
        )


class ManagedHeadersWithStreamingResponse:
    def __init__(self, managed_headers: ManagedHeaders) -> None:
        self._managed_headers = managed_headers

        self.list = to_streamed_response_wrapper(
            managed_headers.list,
        )
        self.managed_transforms_update_status_of_managed_transforms = to_streamed_response_wrapper(
            managed_headers.managed_transforms_update_status_of_managed_transforms,
        )


class AsyncManagedHeadersWithStreamingResponse:
    def __init__(self, managed_headers: AsyncManagedHeaders) -> None:
        self._managed_headers = managed_headers

        self.list = async_to_streamed_response_wrapper(
            managed_headers.list,
        )
        self.managed_transforms_update_status_of_managed_transforms = async_to_streamed_response_wrapper(
            managed_headers.managed_transforms_update_status_of_managed_transforms,
        )
