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
from ...._base_client import (
    make_request_options,
)
from ....types.zones.settings import HTTP2, http2_edit_params

__all__ = ["HTTP2Resource", "AsyncHTTP2Resource"]


class HTTP2Resource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HTTP2ResourceWithRawResponse:
        return HTTP2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HTTP2ResourceWithStreamingResponse:
        return HTTP2ResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HTTP2]:
        """
        Value of the HTTP2 setting.

        Args:
          zone_id: Identifier

          value: Value of the HTTP2 setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/http2",
            body=maybe_transform({"value": value}, http2_edit_params.HTTP2EditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[HTTP2]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[HTTP2]], ResultWrapper[HTTP2]),
        )

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
    ) -> Optional[HTTP2]:
        """
        Value of the HTTP2 setting.

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
            f"/zones/{zone_id}/settings/http2",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[HTTP2]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[HTTP2]], ResultWrapper[HTTP2]),
        )


class AsyncHTTP2Resource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHTTP2ResourceWithRawResponse:
        return AsyncHTTP2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHTTP2ResourceWithStreamingResponse:
        return AsyncHTTP2ResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HTTP2]:
        """
        Value of the HTTP2 setting.

        Args:
          zone_id: Identifier

          value: Value of the HTTP2 setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/http2",
            body=await async_maybe_transform({"value": value}, http2_edit_params.HTTP2EditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[HTTP2]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[HTTP2]], ResultWrapper[HTTP2]),
        )

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
    ) -> Optional[HTTP2]:
        """
        Value of the HTTP2 setting.

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
            f"/zones/{zone_id}/settings/http2",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[HTTP2]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[HTTP2]], ResultWrapper[HTTP2]),
        )


class HTTP2ResourceWithRawResponse:
    def __init__(self, http2: HTTP2Resource) -> None:
        self._http2 = http2

        self.edit = to_raw_response_wrapper(
            http2.edit,
        )
        self.get = to_raw_response_wrapper(
            http2.get,
        )


class AsyncHTTP2ResourceWithRawResponse:
    def __init__(self, http2: AsyncHTTP2Resource) -> None:
        self._http2 = http2

        self.edit = async_to_raw_response_wrapper(
            http2.edit,
        )
        self.get = async_to_raw_response_wrapper(
            http2.get,
        )


class HTTP2ResourceWithStreamingResponse:
    def __init__(self, http2: HTTP2Resource) -> None:
        self._http2 = http2

        self.edit = to_streamed_response_wrapper(
            http2.edit,
        )
        self.get = to_streamed_response_wrapper(
            http2.get,
        )


class AsyncHTTP2ResourceWithStreamingResponse:
    def __init__(self, http2: AsyncHTTP2Resource) -> None:
        self._http2 = http2

        self.edit = async_to_streamed_response_wrapper(
            http2.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            http2.get,
        )
