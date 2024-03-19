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
from ....types.zones.settings import ZonesAlwaysOnline, always_online_edit_params

__all__ = ["AlwaysOnline", "AsyncAlwaysOnline"]


class AlwaysOnline(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AlwaysOnlineWithRawResponse:
        return AlwaysOnlineWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AlwaysOnlineWithStreamingResponse:
        return AlwaysOnlineWithStreamingResponse(self)

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
    ) -> Optional[ZonesAlwaysOnline]:
        """
        When enabled, Cloudflare serves limited copies of web pages available from the
        [Internet Archive's Wayback Machine](https://archive.org/web/) if your server is
        offline. Refer to
        [Always Online](https://developers.cloudflare.com/cache/about/always-online) for
        more information.

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
            f"/zones/{zone_id}/settings/always_online",
            body=maybe_transform({"value": value}, always_online_edit_params.AlwaysOnlineEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesAlwaysOnline]], ResultWrapper[ZonesAlwaysOnline]),
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
    ) -> Optional[ZonesAlwaysOnline]:
        """
        When enabled, Cloudflare serves limited copies of web pages available from the
        [Internet Archive's Wayback Machine](https://archive.org/web/) if your server is
        offline. Refer to
        [Always Online](https://developers.cloudflare.com/cache/about/always-online) for
        more information.

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
            f"/zones/{zone_id}/settings/always_online",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesAlwaysOnline]], ResultWrapper[ZonesAlwaysOnline]),
        )


class AsyncAlwaysOnline(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAlwaysOnlineWithRawResponse:
        return AsyncAlwaysOnlineWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAlwaysOnlineWithStreamingResponse:
        return AsyncAlwaysOnlineWithStreamingResponse(self)

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
    ) -> Optional[ZonesAlwaysOnline]:
        """
        When enabled, Cloudflare serves limited copies of web pages available from the
        [Internet Archive's Wayback Machine](https://archive.org/web/) if your server is
        offline. Refer to
        [Always Online](https://developers.cloudflare.com/cache/about/always-online) for
        more information.

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
            f"/zones/{zone_id}/settings/always_online",
            body=await async_maybe_transform({"value": value}, always_online_edit_params.AlwaysOnlineEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesAlwaysOnline]], ResultWrapper[ZonesAlwaysOnline]),
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
    ) -> Optional[ZonesAlwaysOnline]:
        """
        When enabled, Cloudflare serves limited copies of web pages available from the
        [Internet Archive's Wayback Machine](https://archive.org/web/) if your server is
        offline. Refer to
        [Always Online](https://developers.cloudflare.com/cache/about/always-online) for
        more information.

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
            f"/zones/{zone_id}/settings/always_online",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesAlwaysOnline]], ResultWrapper[ZonesAlwaysOnline]),
        )


class AlwaysOnlineWithRawResponse:
    def __init__(self, always_online: AlwaysOnline) -> None:
        self._always_online = always_online

        self.edit = to_raw_response_wrapper(
            always_online.edit,
        )
        self.get = to_raw_response_wrapper(
            always_online.get,
        )


class AsyncAlwaysOnlineWithRawResponse:
    def __init__(self, always_online: AsyncAlwaysOnline) -> None:
        self._always_online = always_online

        self.edit = async_to_raw_response_wrapper(
            always_online.edit,
        )
        self.get = async_to_raw_response_wrapper(
            always_online.get,
        )


class AlwaysOnlineWithStreamingResponse:
    def __init__(self, always_online: AlwaysOnline) -> None:
        self._always_online = always_online

        self.edit = to_streamed_response_wrapper(
            always_online.edit,
        )
        self.get = to_streamed_response_wrapper(
            always_online.get,
        )


class AsyncAlwaysOnlineWithStreamingResponse:
    def __init__(self, always_online: AsyncAlwaysOnline) -> None:
        self._always_online = always_online

        self.edit = async_to_streamed_response_wrapper(
            always_online.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            always_online.get,
        )
