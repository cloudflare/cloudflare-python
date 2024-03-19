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
from ....types.zones.settings import ZonesWAF, waf_edit_params

__all__ = ["WAF", "AsyncWAF"]


class WAF(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WAFWithRawResponse:
        return WAFWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WAFWithStreamingResponse:
        return WAFWithStreamingResponse(self)

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
    ) -> Optional[ZonesWAF]:
        """The WAF examines HTTP requests to your website.

        It inspects both GET and POST
        requests and applies rules to help filter out illegitimate traffic from
        legitimate website visitors. The Cloudflare WAF inspects website addresses or
        URLs to detect anything out of the ordinary. If the Cloudflare WAF determines
        suspicious user behavior, then the WAF will 'challenge' the web visitor with a
        page that asks them to submit a CAPTCHA successfully to continue their action.
        If the challenge is failed, the action will be stopped. What this means is that
        Cloudflare's WAF will block any traffic identified as illegitimate before it
        reaches your origin web server.
        (https://support.cloudflare.com/hc/en-us/articles/200172016).

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
            f"/zones/{zone_id}/settings/waf",
            body=maybe_transform({"value": value}, waf_edit_params.WAFEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesWAF]], ResultWrapper[ZonesWAF]),
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
    ) -> Optional[ZonesWAF]:
        """The WAF examines HTTP requests to your website.

        It inspects both GET and POST
        requests and applies rules to help filter out illegitimate traffic from
        legitimate website visitors. The Cloudflare WAF inspects website addresses or
        URLs to detect anything out of the ordinary. If the Cloudflare WAF determines
        suspicious user behavior, then the WAF will 'challenge' the web visitor with a
        page that asks them to submit a CAPTCHA successfully to continue their action.
        If the challenge is failed, the action will be stopped. What this means is that
        Cloudflare's WAF will block any traffic identified as illegitimate before it
        reaches your origin web server.
        (https://support.cloudflare.com/hc/en-us/articles/200172016).

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
            f"/zones/{zone_id}/settings/waf",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesWAF]], ResultWrapper[ZonesWAF]),
        )


class AsyncWAF(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWAFWithRawResponse:
        return AsyncWAFWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWAFWithStreamingResponse:
        return AsyncWAFWithStreamingResponse(self)

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
    ) -> Optional[ZonesWAF]:
        """The WAF examines HTTP requests to your website.

        It inspects both GET and POST
        requests and applies rules to help filter out illegitimate traffic from
        legitimate website visitors. The Cloudflare WAF inspects website addresses or
        URLs to detect anything out of the ordinary. If the Cloudflare WAF determines
        suspicious user behavior, then the WAF will 'challenge' the web visitor with a
        page that asks them to submit a CAPTCHA successfully to continue their action.
        If the challenge is failed, the action will be stopped. What this means is that
        Cloudflare's WAF will block any traffic identified as illegitimate before it
        reaches your origin web server.
        (https://support.cloudflare.com/hc/en-us/articles/200172016).

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
            f"/zones/{zone_id}/settings/waf",
            body=await async_maybe_transform({"value": value}, waf_edit_params.WAFEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesWAF]], ResultWrapper[ZonesWAF]),
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
    ) -> Optional[ZonesWAF]:
        """The WAF examines HTTP requests to your website.

        It inspects both GET and POST
        requests and applies rules to help filter out illegitimate traffic from
        legitimate website visitors. The Cloudflare WAF inspects website addresses or
        URLs to detect anything out of the ordinary. If the Cloudflare WAF determines
        suspicious user behavior, then the WAF will 'challenge' the web visitor with a
        page that asks them to submit a CAPTCHA successfully to continue their action.
        If the challenge is failed, the action will be stopped. What this means is that
        Cloudflare's WAF will block any traffic identified as illegitimate before it
        reaches your origin web server.
        (https://support.cloudflare.com/hc/en-us/articles/200172016).

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
            f"/zones/{zone_id}/settings/waf",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesWAF]], ResultWrapper[ZonesWAF]),
        )


class WAFWithRawResponse:
    def __init__(self, waf: WAF) -> None:
        self._waf = waf

        self.edit = to_raw_response_wrapper(
            waf.edit,
        )
        self.get = to_raw_response_wrapper(
            waf.get,
        )


class AsyncWAFWithRawResponse:
    def __init__(self, waf: AsyncWAF) -> None:
        self._waf = waf

        self.edit = async_to_raw_response_wrapper(
            waf.edit,
        )
        self.get = async_to_raw_response_wrapper(
            waf.get,
        )


class WAFWithStreamingResponse:
    def __init__(self, waf: WAF) -> None:
        self._waf = waf

        self.edit = to_streamed_response_wrapper(
            waf.edit,
        )
        self.get = to_streamed_response_wrapper(
            waf.get,
        )


class AsyncWAFWithStreamingResponse:
    def __init__(self, waf: AsyncWAF) -> None:
        self._waf = waf

        self.edit = async_to_streamed_response_wrapper(
            waf.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            waf.get,
        )
