# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
from ....types.magic_network_monitoring import MagicVisibilityMNMConfig

__all__ = ["Full", "AsyncFull"]


class Full(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FullWithRawResponse:
        return FullWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FullWithStreamingResponse:
        return FullWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MagicVisibilityMNMConfig:
        """
        Lists default sampling, router IPs, and rules for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/mnm/config/full",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[MagicVisibilityMNMConfig], ResultWrapper[MagicVisibilityMNMConfig]),
        )


class AsyncFull(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFullWithRawResponse:
        return AsyncFullWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFullWithStreamingResponse:
        return AsyncFullWithStreamingResponse(self)

    async def get(
        self,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MagicVisibilityMNMConfig:
        """
        Lists default sampling, router IPs, and rules for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/mnm/config/full",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[MagicVisibilityMNMConfig], ResultWrapper[MagicVisibilityMNMConfig]),
        )


class FullWithRawResponse:
    def __init__(self, full: Full) -> None:
        self._full = full

        self.get = to_raw_response_wrapper(
            full.get,
        )


class AsyncFullWithRawResponse:
    def __init__(self, full: AsyncFull) -> None:
        self._full = full

        self.get = async_to_raw_response_wrapper(
            full.get,
        )


class FullWithStreamingResponse:
    def __init__(self, full: Full) -> None:
        self._full = full

        self.get = to_streamed_response_wrapper(
            full.get,
        )


class AsyncFullWithStreamingResponse:
    def __init__(self, full: AsyncFull) -> None:
        self._full = full

        self.get = async_to_streamed_response_wrapper(
            full.get,
        )
