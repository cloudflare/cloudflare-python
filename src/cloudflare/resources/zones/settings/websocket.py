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
from ....types.zones.settings import Websocket, websocket_edit_params

__all__ = ["WebsocketResource", "AsyncWebsocketResource"]


class WebsocketResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebsocketResourceWithRawResponse:
        return WebsocketResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebsocketResourceWithStreamingResponse:
        return WebsocketResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: Literal["off", "on"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Websocket]:
        """Changes Websockets setting.

        For more information about Websockets, please refer
        to
        [Using Cloudflare with WebSockets](https://support.cloudflare.com/hc/en-us/articles/200169466-Using-Cloudflare-with-WebSockets).

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/websockets",
            body=maybe_transform({"value": value}, websocket_edit_params.WebsocketEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[Websocket]], ResultWrapper[Websocket]),
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
    ) -> Optional[Websocket]:
        """Gets Websockets setting.

        For more information about Websockets, please refer to
        [Using Cloudflare with WebSockets](https://support.cloudflare.com/hc/en-us/articles/200169466-Using-Cloudflare-with-WebSockets).

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
            f"/zones/{zone_id}/settings/websockets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[Websocket]], ResultWrapper[Websocket]),
        )


class AsyncWebsocketResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebsocketResourceWithRawResponse:
        return AsyncWebsocketResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebsocketResourceWithStreamingResponse:
        return AsyncWebsocketResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: Literal["off", "on"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Websocket]:
        """Changes Websockets setting.

        For more information about Websockets, please refer
        to
        [Using Cloudflare with WebSockets](https://support.cloudflare.com/hc/en-us/articles/200169466-Using-Cloudflare-with-WebSockets).

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/websockets",
            body=await async_maybe_transform({"value": value}, websocket_edit_params.WebsocketEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[Websocket]], ResultWrapper[Websocket]),
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
    ) -> Optional[Websocket]:
        """Gets Websockets setting.

        For more information about Websockets, please refer to
        [Using Cloudflare with WebSockets](https://support.cloudflare.com/hc/en-us/articles/200169466-Using-Cloudflare-with-WebSockets).

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
            f"/zones/{zone_id}/settings/websockets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[Websocket]], ResultWrapper[Websocket]),
        )


class WebsocketResourceWithRawResponse:
    def __init__(self, websocket: WebsocketResource) -> None:
        self._websocket = websocket

        self.edit = to_raw_response_wrapper(
            websocket.edit,
        )
        self.get = to_raw_response_wrapper(
            websocket.get,
        )


class AsyncWebsocketResourceWithRawResponse:
    def __init__(self, websocket: AsyncWebsocketResource) -> None:
        self._websocket = websocket

        self.edit = async_to_raw_response_wrapper(
            websocket.edit,
        )
        self.get = async_to_raw_response_wrapper(
            websocket.get,
        )


class WebsocketResourceWithStreamingResponse:
    def __init__(self, websocket: WebsocketResource) -> None:
        self._websocket = websocket

        self.edit = to_streamed_response_wrapper(
            websocket.edit,
        )
        self.get = to_streamed_response_wrapper(
            websocket.get,
        )


class AsyncWebsocketResourceWithStreamingResponse:
    def __init__(self, websocket: AsyncWebsocketResource) -> None:
        self._websocket = websocket

        self.edit = async_to_streamed_response_wrapper(
            websocket.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            websocket.get,
        )
