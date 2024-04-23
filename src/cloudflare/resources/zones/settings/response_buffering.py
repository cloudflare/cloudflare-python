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
from ....types.zones.settings import response_buffering_edit_params
from ....types.zones.settings.response_buffering import ResponseBuffering

__all__ = ["ResponseBufferingResource", "AsyncResponseBufferingResource"]


class ResponseBufferingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResponseBufferingResourceWithRawResponse:
        return ResponseBufferingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResponseBufferingResourceWithStreamingResponse:
        return ResponseBufferingResourceWithStreamingResponse(self)

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
    ) -> Optional[ResponseBuffering]:
        """Enables or disables buffering of responses from the proxied server.

        Cloudflare
        may buffer the whole payload to deliver it at once to the client versus allowing
        it to be delivered in chunks. By default, the proxied server streams directly
        and is not buffered by Cloudflare. This is limited to Enterprise Zones.

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
            f"/zones/{zone_id}/settings/response_buffering",
            body=maybe_transform({"value": value}, response_buffering_edit_params.ResponseBufferingEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ResponseBuffering]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ResponseBuffering]], ResultWrapper[ResponseBuffering]),
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
    ) -> Optional[ResponseBuffering]:
        """Enables or disables buffering of responses from the proxied server.

        Cloudflare
        may buffer the whole payload to deliver it at once to the client versus allowing
        it to be delivered in chunks. By default, the proxied server streams directly
        and is not buffered by Cloudflare. This is limited to Enterprise Zones.

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
            f"/zones/{zone_id}/settings/response_buffering",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ResponseBuffering]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ResponseBuffering]], ResultWrapper[ResponseBuffering]),
        )


class AsyncResponseBufferingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResponseBufferingResourceWithRawResponse:
        return AsyncResponseBufferingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResponseBufferingResourceWithStreamingResponse:
        return AsyncResponseBufferingResourceWithStreamingResponse(self)

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
    ) -> Optional[ResponseBuffering]:
        """Enables or disables buffering of responses from the proxied server.

        Cloudflare
        may buffer the whole payload to deliver it at once to the client versus allowing
        it to be delivered in chunks. By default, the proxied server streams directly
        and is not buffered by Cloudflare. This is limited to Enterprise Zones.

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
            f"/zones/{zone_id}/settings/response_buffering",
            body=await async_maybe_transform(
                {"value": value}, response_buffering_edit_params.ResponseBufferingEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ResponseBuffering]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ResponseBuffering]], ResultWrapper[ResponseBuffering]),
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
    ) -> Optional[ResponseBuffering]:
        """Enables or disables buffering of responses from the proxied server.

        Cloudflare
        may buffer the whole payload to deliver it at once to the client versus allowing
        it to be delivered in chunks. By default, the proxied server streams directly
        and is not buffered by Cloudflare. This is limited to Enterprise Zones.

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
            f"/zones/{zone_id}/settings/response_buffering",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ResponseBuffering]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ResponseBuffering]], ResultWrapper[ResponseBuffering]),
        )


class ResponseBufferingResourceWithRawResponse:
    def __init__(self, response_buffering: ResponseBufferingResource) -> None:
        self._response_buffering = response_buffering

        self.edit = to_raw_response_wrapper(
            response_buffering.edit,
        )
        self.get = to_raw_response_wrapper(
            response_buffering.get,
        )


class AsyncResponseBufferingResourceWithRawResponse:
    def __init__(self, response_buffering: AsyncResponseBufferingResource) -> None:
        self._response_buffering = response_buffering

        self.edit = async_to_raw_response_wrapper(
            response_buffering.edit,
        )
        self.get = async_to_raw_response_wrapper(
            response_buffering.get,
        )


class ResponseBufferingResourceWithStreamingResponse:
    def __init__(self, response_buffering: ResponseBufferingResource) -> None:
        self._response_buffering = response_buffering

        self.edit = to_streamed_response_wrapper(
            response_buffering.edit,
        )
        self.get = to_streamed_response_wrapper(
            response_buffering.get,
        )


class AsyncResponseBufferingResourceWithStreamingResponse:
    def __init__(self, response_buffering: AsyncResponseBufferingResource) -> None:
        self._response_buffering = response_buffering

        self.edit = async_to_streamed_response_wrapper(
            response_buffering.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            response_buffering.get,
        )
