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
from ....types.zones.settings import ZonesServerSideExclude, server_side_exclude_edit_params

__all__ = ["ServerSideExcludes", "AsyncServerSideExcludes"]


class ServerSideExcludes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ServerSideExcludesWithRawResponse:
        return ServerSideExcludesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServerSideExcludesWithStreamingResponse:
        return ServerSideExcludesWithStreamingResponse(self)

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
    ) -> Optional[ZonesServerSideExclude]:
        """
        If there is sensitive content on your website that you want visible to real
        visitors, but that you want to hide from suspicious visitors, all you have to do
        is wrap the content with Cloudflare SSE tags. Wrap any content that you want to
        be excluded from suspicious visitors in the following SSE tags:
        <!--sse--><!--/sse-->. For example: <!--sse--> Bad visitors won't see my phone
        number, 555-555-5555 <!--/sse-->. Note: SSE only will work with HTML. If you
        have HTML minification enabled, you won't see the SSE tags in your HTML source
        when it's served through Cloudflare. SSE will still function in this case, as
        Cloudflare's HTML minification and SSE functionality occur on-the-fly as the
        resource moves through our network to the visitor's computer.
        (https://support.cloudflare.com/hc/en-us/articles/200170036).

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
            f"/zones/{zone_id}/settings/server_side_exclude",
            body=maybe_transform({"value": value}, server_side_exclude_edit_params.ServerSideExcludeEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesServerSideExclude]], ResultWrapper[ZonesServerSideExclude]),
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
    ) -> Optional[ZonesServerSideExclude]:
        """
        If there is sensitive content on your website that you want visible to real
        visitors, but that you want to hide from suspicious visitors, all you have to do
        is wrap the content with Cloudflare SSE tags. Wrap any content that you want to
        be excluded from suspicious visitors in the following SSE tags:
        <!--sse--><!--/sse-->. For example: <!--sse--> Bad visitors won't see my phone
        number, 555-555-5555 <!--/sse-->. Note: SSE only will work with HTML. If you
        have HTML minification enabled, you won't see the SSE tags in your HTML source
        when it's served through Cloudflare. SSE will still function in this case, as
        Cloudflare's HTML minification and SSE functionality occur on-the-fly as the
        resource moves through our network to the visitor's computer.
        (https://support.cloudflare.com/hc/en-us/articles/200170036).

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
            f"/zones/{zone_id}/settings/server_side_exclude",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesServerSideExclude]], ResultWrapper[ZonesServerSideExclude]),
        )


class AsyncServerSideExcludes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncServerSideExcludesWithRawResponse:
        return AsyncServerSideExcludesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServerSideExcludesWithStreamingResponse:
        return AsyncServerSideExcludesWithStreamingResponse(self)

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
    ) -> Optional[ZonesServerSideExclude]:
        """
        If there is sensitive content on your website that you want visible to real
        visitors, but that you want to hide from suspicious visitors, all you have to do
        is wrap the content with Cloudflare SSE tags. Wrap any content that you want to
        be excluded from suspicious visitors in the following SSE tags:
        <!--sse--><!--/sse-->. For example: <!--sse--> Bad visitors won't see my phone
        number, 555-555-5555 <!--/sse-->. Note: SSE only will work with HTML. If you
        have HTML minification enabled, you won't see the SSE tags in your HTML source
        when it's served through Cloudflare. SSE will still function in this case, as
        Cloudflare's HTML minification and SSE functionality occur on-the-fly as the
        resource moves through our network to the visitor's computer.
        (https://support.cloudflare.com/hc/en-us/articles/200170036).

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
            f"/zones/{zone_id}/settings/server_side_exclude",
            body=await async_maybe_transform(
                {"value": value}, server_side_exclude_edit_params.ServerSideExcludeEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesServerSideExclude]], ResultWrapper[ZonesServerSideExclude]),
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
    ) -> Optional[ZonesServerSideExclude]:
        """
        If there is sensitive content on your website that you want visible to real
        visitors, but that you want to hide from suspicious visitors, all you have to do
        is wrap the content with Cloudflare SSE tags. Wrap any content that you want to
        be excluded from suspicious visitors in the following SSE tags:
        <!--sse--><!--/sse-->. For example: <!--sse--> Bad visitors won't see my phone
        number, 555-555-5555 <!--/sse-->. Note: SSE only will work with HTML. If you
        have HTML minification enabled, you won't see the SSE tags in your HTML source
        when it's served through Cloudflare. SSE will still function in this case, as
        Cloudflare's HTML minification and SSE functionality occur on-the-fly as the
        resource moves through our network to the visitor's computer.
        (https://support.cloudflare.com/hc/en-us/articles/200170036).

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
            f"/zones/{zone_id}/settings/server_side_exclude",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesServerSideExclude]], ResultWrapper[ZonesServerSideExclude]),
        )


class ServerSideExcludesWithRawResponse:
    def __init__(self, server_side_excludes: ServerSideExcludes) -> None:
        self._server_side_excludes = server_side_excludes

        self.edit = to_raw_response_wrapper(
            server_side_excludes.edit,
        )
        self.get = to_raw_response_wrapper(
            server_side_excludes.get,
        )


class AsyncServerSideExcludesWithRawResponse:
    def __init__(self, server_side_excludes: AsyncServerSideExcludes) -> None:
        self._server_side_excludes = server_side_excludes

        self.edit = async_to_raw_response_wrapper(
            server_side_excludes.edit,
        )
        self.get = async_to_raw_response_wrapper(
            server_side_excludes.get,
        )


class ServerSideExcludesWithStreamingResponse:
    def __init__(self, server_side_excludes: ServerSideExcludes) -> None:
        self._server_side_excludes = server_side_excludes

        self.edit = to_streamed_response_wrapper(
            server_side_excludes.edit,
        )
        self.get = to_streamed_response_wrapper(
            server_side_excludes.get,
        )


class AsyncServerSideExcludesWithStreamingResponse:
    def __init__(self, server_side_excludes: AsyncServerSideExcludes) -> None:
        self._server_side_excludes = server_side_excludes

        self.edit = async_to_streamed_response_wrapper(
            server_side_excludes.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            server_side_excludes.get,
        )
