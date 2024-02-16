# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.zaraz import DefaultGetResponse
from ..._base_client import (
    make_request_options,
)

__all__ = ["Default", "AsyncDefault"]


class Default(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DefaultWithRawResponse:
        return DefaultWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DefaultWithStreamingResponse:
        return DefaultWithStreamingResponse(self)

    def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DefaultGetResponse:
        """
        Gets default Zaraz configuration for a zone.

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
            f"/zones/{zone_id}/settings/zaraz/default",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DefaultGetResponse], ResultWrapper[DefaultGetResponse]),
        )


class AsyncDefault(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDefaultWithRawResponse:
        return AsyncDefaultWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDefaultWithStreamingResponse:
        return AsyncDefaultWithStreamingResponse(self)

    async def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DefaultGetResponse:
        """
        Gets default Zaraz configuration for a zone.

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
            f"/zones/{zone_id}/settings/zaraz/default",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DefaultGetResponse], ResultWrapper[DefaultGetResponse]),
        )


class DefaultWithRawResponse:
    def __init__(self, default: Default) -> None:
        self._default = default

        self.get = to_raw_response_wrapper(
            default.get,
        )


class AsyncDefaultWithRawResponse:
    def __init__(self, default: AsyncDefault) -> None:
        self._default = default

        self.get = async_to_raw_response_wrapper(
            default.get,
        )


class DefaultWithStreamingResponse:
    def __init__(self, default: Default) -> None:
        self._default = default

        self.get = to_streamed_response_wrapper(
            default.get,
        )


class AsyncDefaultWithStreamingResponse:
    def __init__(self, default: AsyncDefault) -> None:
        self._default = default

        self.get = async_to_streamed_response_wrapper(
            default.get,
        )
