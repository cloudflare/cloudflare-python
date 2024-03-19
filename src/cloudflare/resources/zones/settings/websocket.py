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
from ....types.zones.settings import ZonesWebsockets, websocket_edit_params

__all__ = ["Websocket", "AsyncWebsocket"]


class Websocket(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebsocketWithRawResponse:
        return WebsocketWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebsocketWithStreamingResponse:
        return WebsocketWithStreamingResponse(self)

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
    ) -> Optional[ZonesWebsockets]:
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
            cast_to=cast(Type[Optional[ZonesWebsockets]], ResultWrapper[ZonesWebsockets]),
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
    ) -> Optional[ZonesWebsockets]:
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
            cast_to=cast(Type[Optional[ZonesWebsockets]], ResultWrapper[ZonesWebsockets]),
        )


class AsyncWebsocket(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebsocketWithRawResponse:
        return AsyncWebsocketWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebsocketWithStreamingResponse:
        return AsyncWebsocketWithStreamingResponse(self)

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
    ) -> Optional[ZonesWebsockets]:
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
            cast_to=cast(Type[Optional[ZonesWebsockets]], ResultWrapper[ZonesWebsockets]),
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
    ) -> Optional[ZonesWebsockets]:
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
            cast_to=cast(Type[Optional[ZonesWebsockets]], ResultWrapper[ZonesWebsockets]),
        )


class WebsocketWithRawResponse:
    def __init__(self, websocket: Websocket) -> None:
        self._websocket = websocket

        self.edit = to_raw_response_wrapper(
            websocket.edit,
        )
        self.get = to_raw_response_wrapper(
            websocket.get,
        )


class AsyncWebsocketWithRawResponse:
    def __init__(self, websocket: AsyncWebsocket) -> None:
        self._websocket = websocket

        self.edit = async_to_raw_response_wrapper(
            websocket.edit,
        )
        self.get = async_to_raw_response_wrapper(
            websocket.get,
        )


class WebsocketWithStreamingResponse:
    def __init__(self, websocket: Websocket) -> None:
        self._websocket = websocket

        self.edit = to_streamed_response_wrapper(
            websocket.edit,
        )
        self.get = to_streamed_response_wrapper(
            websocket.get,
        )


class AsyncWebsocketWithStreamingResponse:
    def __init__(self, websocket: AsyncWebsocket) -> None:
        self._websocket = websocket

        self.edit = async_to_streamed_response_wrapper(
            websocket.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            websocket.get,
        )
