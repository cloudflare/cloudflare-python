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
from ....types.zones.settings import browser_check_edit_params
from ....types.zones.settings.browser_check import BrowserCheck

__all__ = ["BrowserCheckResource", "AsyncBrowserCheckResource"]


class BrowserCheckResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BrowserCheckResourceWithRawResponse:
        return BrowserCheckResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrowserCheckResourceWithStreamingResponse:
        return BrowserCheckResourceWithStreamingResponse(self)

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
    ) -> Optional[BrowserCheck]:
        """
        Browser Integrity Check is similar to Bad Behavior and looks for common HTTP
        headers abused most commonly by spammers and denies access to your page. It will
        also challenge visitors that do not have a user agent or a non standard user
        agent (also commonly used by abuse bots, crawlers or visitors).
        (https://support.cloudflare.com/hc/en-us/articles/200170086).

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
            f"/zones/{zone_id}/settings/browser_check",
            body=maybe_transform({"value": value}, browser_check_edit_params.BrowserCheckEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BrowserCheck]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BrowserCheck]], ResultWrapper[BrowserCheck]),
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
    ) -> Optional[BrowserCheck]:
        """
        Browser Integrity Check is similar to Bad Behavior and looks for common HTTP
        headers abused most commonly by spammers and denies access to your page. It will
        also challenge visitors that do not have a user agent or a non standard user
        agent (also commonly used by abuse bots, crawlers or visitors).
        (https://support.cloudflare.com/hc/en-us/articles/200170086).

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
            f"/zones/{zone_id}/settings/browser_check",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BrowserCheck]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BrowserCheck]], ResultWrapper[BrowserCheck]),
        )


class AsyncBrowserCheckResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBrowserCheckResourceWithRawResponse:
        return AsyncBrowserCheckResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrowserCheckResourceWithStreamingResponse:
        return AsyncBrowserCheckResourceWithStreamingResponse(self)

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
    ) -> Optional[BrowserCheck]:
        """
        Browser Integrity Check is similar to Bad Behavior and looks for common HTTP
        headers abused most commonly by spammers and denies access to your page. It will
        also challenge visitors that do not have a user agent or a non standard user
        agent (also commonly used by abuse bots, crawlers or visitors).
        (https://support.cloudflare.com/hc/en-us/articles/200170086).

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
            f"/zones/{zone_id}/settings/browser_check",
            body=await async_maybe_transform({"value": value}, browser_check_edit_params.BrowserCheckEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BrowserCheck]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BrowserCheck]], ResultWrapper[BrowserCheck]),
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
    ) -> Optional[BrowserCheck]:
        """
        Browser Integrity Check is similar to Bad Behavior and looks for common HTTP
        headers abused most commonly by spammers and denies access to your page. It will
        also challenge visitors that do not have a user agent or a non standard user
        agent (also commonly used by abuse bots, crawlers or visitors).
        (https://support.cloudflare.com/hc/en-us/articles/200170086).

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
            f"/zones/{zone_id}/settings/browser_check",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BrowserCheck]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BrowserCheck]], ResultWrapper[BrowserCheck]),
        )


class BrowserCheckResourceWithRawResponse:
    def __init__(self, browser_check: BrowserCheckResource) -> None:
        self._browser_check = browser_check

        self.edit = to_raw_response_wrapper(
            browser_check.edit,
        )
        self.get = to_raw_response_wrapper(
            browser_check.get,
        )


class AsyncBrowserCheckResourceWithRawResponse:
    def __init__(self, browser_check: AsyncBrowserCheckResource) -> None:
        self._browser_check = browser_check

        self.edit = async_to_raw_response_wrapper(
            browser_check.edit,
        )
        self.get = async_to_raw_response_wrapper(
            browser_check.get,
        )


class BrowserCheckResourceWithStreamingResponse:
    def __init__(self, browser_check: BrowserCheckResource) -> None:
        self._browser_check = browser_check

        self.edit = to_streamed_response_wrapper(
            browser_check.edit,
        )
        self.get = to_streamed_response_wrapper(
            browser_check.get,
        )


class AsyncBrowserCheckResourceWithStreamingResponse:
    def __init__(self, browser_check: AsyncBrowserCheckResource) -> None:
        self._browser_check = browser_check

        self.edit = async_to_streamed_response_wrapper(
            browser_check.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            browser_check.get,
        )
