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
from ....types.workers.scripts import BindingGetResponse

__all__ = ["Bindings", "AsyncBindings"]


class Bindings(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BindingsWithRawResponse:
        return BindingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BindingsWithStreamingResponse:
        return BindingsWithStreamingResponse(self)

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BindingGetResponse:
        """
        List the bindings for a Workers script.

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
            f"/zones/{zone_id}/workers/script/bindings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[BindingGetResponse], ResultWrapper[BindingGetResponse]),
        )


class AsyncBindings(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBindingsWithRawResponse:
        return AsyncBindingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBindingsWithStreamingResponse:
        return AsyncBindingsWithStreamingResponse(self)

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BindingGetResponse:
        """
        List the bindings for a Workers script.

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
            f"/zones/{zone_id}/workers/script/bindings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[BindingGetResponse], ResultWrapper[BindingGetResponse]),
        )


class BindingsWithRawResponse:
    def __init__(self, bindings: Bindings) -> None:
        self._bindings = bindings

        self.get = to_raw_response_wrapper(
            bindings.get,
        )


class AsyncBindingsWithRawResponse:
    def __init__(self, bindings: AsyncBindings) -> None:
        self._bindings = bindings

        self.get = async_to_raw_response_wrapper(
            bindings.get,
        )


class BindingsWithStreamingResponse:
    def __init__(self, bindings: Bindings) -> None:
        self._bindings = bindings

        self.get = to_streamed_response_wrapper(
            bindings.get,
        )


class AsyncBindingsWithStreamingResponse:
    def __init__(self, bindings: AsyncBindings) -> None:
        self._bindings = bindings

        self.get = async_to_streamed_response_wrapper(
            bindings.get,
        )
