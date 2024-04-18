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
from ....types.zones.settings import BrowserCacheTTL, browser_cache_ttl_edit_params

__all__ = ["BrowserCacheTTLResource", "AsyncBrowserCacheTTLResource"]


class BrowserCacheTTLResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BrowserCacheTTLResourceWithRawResponse:
        return BrowserCacheTTLResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrowserCacheTTLResourceWithStreamingResponse:
        return BrowserCacheTTLResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: Literal[
            0,
            30,
            60,
            120,
            300,
            1200,
            1800,
            3600,
            7200,
            10800,
            14400,
            18000,
            28800,
            43200,
            57600,
            72000,
            86400,
            172800,
            259200,
            345600,
            432000,
            691200,
            1382400,
            2073600,
            2678400,
            5356800,
            16070400,
            31536000,
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BrowserCacheTTL]:
        """
        Browser Cache TTL (in seconds) specifies how long Cloudflare-cached resources
        will remain on your visitors' computers. Cloudflare will honor any larger times
        specified by your server.
        (https://support.cloudflare.com/hc/en-us/articles/200168276).

        Args:
          zone_id: Identifier

          value: Value of the zone setting. Notes: Setting a TTL of 0 is equivalent to selecting
              `Respect Existing Headers`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/browser_cache_ttl",
            body=maybe_transform({"value": value}, browser_cache_ttl_edit_params.BrowserCacheTTLEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BrowserCacheTTL]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BrowserCacheTTL]], ResultWrapper[BrowserCacheTTL]),
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
    ) -> Optional[BrowserCacheTTL]:
        """
        Browser Cache TTL (in seconds) specifies how long Cloudflare-cached resources
        will remain on your visitors' computers. Cloudflare will honor any larger times
        specified by your server.
        (https://support.cloudflare.com/hc/en-us/articles/200168276).

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
            f"/zones/{zone_id}/settings/browser_cache_ttl",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BrowserCacheTTL]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BrowserCacheTTL]], ResultWrapper[BrowserCacheTTL]),
        )


class AsyncBrowserCacheTTLResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBrowserCacheTTLResourceWithRawResponse:
        return AsyncBrowserCacheTTLResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrowserCacheTTLResourceWithStreamingResponse:
        return AsyncBrowserCacheTTLResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: Literal[
            0,
            30,
            60,
            120,
            300,
            1200,
            1800,
            3600,
            7200,
            10800,
            14400,
            18000,
            28800,
            43200,
            57600,
            72000,
            86400,
            172800,
            259200,
            345600,
            432000,
            691200,
            1382400,
            2073600,
            2678400,
            5356800,
            16070400,
            31536000,
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BrowserCacheTTL]:
        """
        Browser Cache TTL (in seconds) specifies how long Cloudflare-cached resources
        will remain on your visitors' computers. Cloudflare will honor any larger times
        specified by your server.
        (https://support.cloudflare.com/hc/en-us/articles/200168276).

        Args:
          zone_id: Identifier

          value: Value of the zone setting. Notes: Setting a TTL of 0 is equivalent to selecting
              `Respect Existing Headers`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/browser_cache_ttl",
            body=await async_maybe_transform({"value": value}, browser_cache_ttl_edit_params.BrowserCacheTTLEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BrowserCacheTTL]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BrowserCacheTTL]], ResultWrapper[BrowserCacheTTL]),
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
    ) -> Optional[BrowserCacheTTL]:
        """
        Browser Cache TTL (in seconds) specifies how long Cloudflare-cached resources
        will remain on your visitors' computers. Cloudflare will honor any larger times
        specified by your server.
        (https://support.cloudflare.com/hc/en-us/articles/200168276).

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
            f"/zones/{zone_id}/settings/browser_cache_ttl",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BrowserCacheTTL]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BrowserCacheTTL]], ResultWrapper[BrowserCacheTTL]),
        )


class BrowserCacheTTLResourceWithRawResponse:
    def __init__(self, browser_cache_ttl: BrowserCacheTTLResource) -> None:
        self._browser_cache_ttl = browser_cache_ttl

        self.edit = to_raw_response_wrapper(
            browser_cache_ttl.edit,
        )
        self.get = to_raw_response_wrapper(
            browser_cache_ttl.get,
        )


class AsyncBrowserCacheTTLResourceWithRawResponse:
    def __init__(self, browser_cache_ttl: AsyncBrowserCacheTTLResource) -> None:
        self._browser_cache_ttl = browser_cache_ttl

        self.edit = async_to_raw_response_wrapper(
            browser_cache_ttl.edit,
        )
        self.get = async_to_raw_response_wrapper(
            browser_cache_ttl.get,
        )


class BrowserCacheTTLResourceWithStreamingResponse:
    def __init__(self, browser_cache_ttl: BrowserCacheTTLResource) -> None:
        self._browser_cache_ttl = browser_cache_ttl

        self.edit = to_streamed_response_wrapper(
            browser_cache_ttl.edit,
        )
        self.get = to_streamed_response_wrapper(
            browser_cache_ttl.get,
        )


class AsyncBrowserCacheTTLResourceWithStreamingResponse:
    def __init__(self, browser_cache_ttl: AsyncBrowserCacheTTLResource) -> None:
        self._browser_cache_ttl = browser_cache_ttl

        self.edit = async_to_streamed_response_wrapper(
            browser_cache_ttl.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            browser_cache_ttl.get,
        )
