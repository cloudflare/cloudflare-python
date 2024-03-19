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
from ....types.zones.settings import ZonesHTTP2, http2_edit_params

__all__ = ["HTTP2", "AsyncHTTP2"]


class HTTP2(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HTTP2WithRawResponse:
        return HTTP2WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HTTP2WithStreamingResponse:
        return HTTP2WithStreamingResponse(self)

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
    ) -> Optional[ZonesHTTP2]:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesHTTP2]], ResultWrapper[ZonesHTTP2]),
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
    ) -> Optional[ZonesHTTP2]:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesHTTP2]], ResultWrapper[ZonesHTTP2]),
        )


class AsyncHTTP2(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHTTP2WithRawResponse:
        return AsyncHTTP2WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHTTP2WithStreamingResponse:
        return AsyncHTTP2WithStreamingResponse(self)

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
    ) -> Optional[ZonesHTTP2]:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesHTTP2]], ResultWrapper[ZonesHTTP2]),
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
    ) -> Optional[ZonesHTTP2]:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesHTTP2]], ResultWrapper[ZonesHTTP2]),
        )


class HTTP2WithRawResponse:
    def __init__(self, http2: HTTP2) -> None:
        self._http2 = http2

        self.edit = to_raw_response_wrapper(
            http2.edit,
        )
        self.get = to_raw_response_wrapper(
            http2.get,
        )


class AsyncHTTP2WithRawResponse:
    def __init__(self, http2: AsyncHTTP2) -> None:
        self._http2 = http2

        self.edit = async_to_raw_response_wrapper(
            http2.edit,
        )
        self.get = async_to_raw_response_wrapper(
            http2.get,
        )


class HTTP2WithStreamingResponse:
    def __init__(self, http2: HTTP2) -> None:
        self._http2 = http2

        self.edit = to_streamed_response_wrapper(
            http2.edit,
        )
        self.get = to_streamed_response_wrapper(
            http2.get,
        )


class AsyncHTTP2WithStreamingResponse:
    def __init__(self, http2: AsyncHTTP2) -> None:
        self._http2 = http2

        self.edit = async_to_streamed_response_wrapper(
            http2.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            http2.get,
        )
