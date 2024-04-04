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
from ....types.zones.settings import ZeroRTT, zero_rtt_edit_params

__all__ = ["ZeroRTTResource", "AsyncZeroRTTResource"]


class ZeroRTTResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ZeroRTTResourceWithRawResponse:
        return ZeroRTTResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ZeroRTTResourceWithStreamingResponse:
        return ZeroRTTResourceWithStreamingResponse(self)

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
    ) -> Optional[ZeroRTT]:
        """
        Changes the 0-RTT session resumption setting.

        Args:
          zone_id: Identifier

          value: Value of the 0-RTT setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/0rtt",
            body=maybe_transform({"value": value}, zero_rtt_edit_params.ZeroRTTEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZeroRTT]], ResultWrapper[ZeroRTT]),
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
    ) -> Optional[ZeroRTT]:
        """
        Gets 0-RTT session resumption setting.

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
            f"/zones/{zone_id}/settings/0rtt",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZeroRTT]], ResultWrapper[ZeroRTT]),
        )


class AsyncZeroRTTResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncZeroRTTResourceWithRawResponse:
        return AsyncZeroRTTResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncZeroRTTResourceWithStreamingResponse:
        return AsyncZeroRTTResourceWithStreamingResponse(self)

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
    ) -> Optional[ZeroRTT]:
        """
        Changes the 0-RTT session resumption setting.

        Args:
          zone_id: Identifier

          value: Value of the 0-RTT setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/0rtt",
            body=await async_maybe_transform({"value": value}, zero_rtt_edit_params.ZeroRTTEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZeroRTT]], ResultWrapper[ZeroRTT]),
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
    ) -> Optional[ZeroRTT]:
        """
        Gets 0-RTT session resumption setting.

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
            f"/zones/{zone_id}/settings/0rtt",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZeroRTT]], ResultWrapper[ZeroRTT]),
        )


class ZeroRTTResourceWithRawResponse:
    def __init__(self, zero_rtt: ZeroRTTResource) -> None:
        self._zero_rtt = zero_rtt

        self.edit = to_raw_response_wrapper(
            zero_rtt.edit,
        )
        self.get = to_raw_response_wrapper(
            zero_rtt.get,
        )


class AsyncZeroRTTResourceWithRawResponse:
    def __init__(self, zero_rtt: AsyncZeroRTTResource) -> None:
        self._zero_rtt = zero_rtt

        self.edit = async_to_raw_response_wrapper(
            zero_rtt.edit,
        )
        self.get = async_to_raw_response_wrapper(
            zero_rtt.get,
        )


class ZeroRTTResourceWithStreamingResponse:
    def __init__(self, zero_rtt: ZeroRTTResource) -> None:
        self._zero_rtt = zero_rtt

        self.edit = to_streamed_response_wrapper(
            zero_rtt.edit,
        )
        self.get = to_streamed_response_wrapper(
            zero_rtt.get,
        )


class AsyncZeroRTTResourceWithStreamingResponse:
    def __init__(self, zero_rtt: AsyncZeroRTTResource) -> None:
        self._zero_rtt = zero_rtt

        self.edit = async_to_streamed_response_wrapper(
            zero_rtt.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            zero_rtt.get,
        )
