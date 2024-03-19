# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import ManagedHeaderEditResponse, ManagedHeaderListResponse, managed_header_edit_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)

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
        *,
        zone_id: str,
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

    def edit(
        self,
        *,
        zone_id: str,
        managed_request_headers: Iterable[managed_header_edit_params.ManagedRequestHeader],
        managed_response_headers: Iterable[managed_header_edit_params.ManagedResponseHeader],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ManagedHeaderEditResponse:
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
                managed_header_edit_params.ManagedHeaderEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagedHeaderEditResponse,
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
        *,
        zone_id: str,
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

    async def edit(
        self,
        *,
        zone_id: str,
        managed_request_headers: Iterable[managed_header_edit_params.ManagedRequestHeader],
        managed_response_headers: Iterable[managed_header_edit_params.ManagedResponseHeader],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ManagedHeaderEditResponse:
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
            body=await async_maybe_transform(
                {
                    "managed_request_headers": managed_request_headers,
                    "managed_response_headers": managed_response_headers,
                },
                managed_header_edit_params.ManagedHeaderEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagedHeaderEditResponse,
        )


class ManagedHeadersWithRawResponse:
    def __init__(self, managed_headers: ManagedHeaders) -> None:
        self._managed_headers = managed_headers

        self.list = to_raw_response_wrapper(
            managed_headers.list,
        )
        self.edit = to_raw_response_wrapper(
            managed_headers.edit,
        )


class AsyncManagedHeadersWithRawResponse:
    def __init__(self, managed_headers: AsyncManagedHeaders) -> None:
        self._managed_headers = managed_headers

        self.list = async_to_raw_response_wrapper(
            managed_headers.list,
        )
        self.edit = async_to_raw_response_wrapper(
            managed_headers.edit,
        )


class ManagedHeadersWithStreamingResponse:
    def __init__(self, managed_headers: ManagedHeaders) -> None:
        self._managed_headers = managed_headers

        self.list = to_streamed_response_wrapper(
            managed_headers.list,
        )
        self.edit = to_streamed_response_wrapper(
            managed_headers.edit,
        )


class AsyncManagedHeadersWithStreamingResponse:
    def __init__(self, managed_headers: AsyncManagedHeaders) -> None:
        self._managed_headers = managed_headers

        self.list = async_to_streamed_response_wrapper(
            managed_headers.list,
        )
        self.edit = async_to_streamed_response_wrapper(
            managed_headers.edit,
        )
