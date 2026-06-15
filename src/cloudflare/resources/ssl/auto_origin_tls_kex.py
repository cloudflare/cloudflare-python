# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.ssl import auto_origin_tls_kex_edit_params
from ..._base_client import make_request_options
from ...types.ssl.auto_origin_tls_kex_get_response import AutoOriginTLSKexGetResponse
from ...types.ssl.auto_origin_tls_kex_edit_response import AutoOriginTLSKexEditResponse

__all__ = ["AutoOriginTLSKexResource", "AsyncAutoOriginTLSKexResource"]


class AutoOriginTLSKexResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AutoOriginTLSKexResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AutoOriginTLSKexResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutoOriginTLSKexResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AutoOriginTLSKexResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoOriginTLSKexEditResponse:
        """
        Enable or disable Auto-Origin TLS KEX selection for the zone by sending
        `{"enabled": true}` or `{"enabled": false}`. When enabled, Cloudflare runs a
        periodic scan of the zone's origins to determine the preferred key-exchange
        algorithm and writes that preference to the edge so it is sent first in the TLS
        ClientHello to the origin.

        Args:
          enabled: Controls enablement of Auto-Origin TLS KEX selection for the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            path_template("/zones/{zone_id}/settings/auto_origin_tls_kex", zone_id=zone_id),
            body=maybe_transform({"enabled": enabled}, auto_origin_tls_kex_edit_params.AutoOriginTLSKexEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AutoOriginTLSKexEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[AutoOriginTLSKexEditResponse], ResultWrapper[AutoOriginTLSKexEditResponse]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoOriginTLSKexGetResponse:
        """
        When enabled, Cloudflare automatically selects the preferred TLS key-exchange
        algorithm to use when establishing the TLS connection to the zone's origin,
        picking from the algorithms permitted by the zone's
        `origin_tls_compliance_modes` setting. When disabled, the default key-exchange
        ordering is used.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            path_template("/zones/{zone_id}/settings/auto_origin_tls_kex", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AutoOriginTLSKexGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[AutoOriginTLSKexGetResponse], ResultWrapper[AutoOriginTLSKexGetResponse]),
        )


class AsyncAutoOriginTLSKexResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAutoOriginTLSKexResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAutoOriginTLSKexResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutoOriginTLSKexResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAutoOriginTLSKexResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoOriginTLSKexEditResponse:
        """
        Enable or disable Auto-Origin TLS KEX selection for the zone by sending
        `{"enabled": true}` or `{"enabled": false}`. When enabled, Cloudflare runs a
        periodic scan of the zone's origins to determine the preferred key-exchange
        algorithm and writes that preference to the edge so it is sent first in the TLS
        ClientHello to the origin.

        Args:
          enabled: Controls enablement of Auto-Origin TLS KEX selection for the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            path_template("/zones/{zone_id}/settings/auto_origin_tls_kex", zone_id=zone_id),
            body=await async_maybe_transform(
                {"enabled": enabled}, auto_origin_tls_kex_edit_params.AutoOriginTLSKexEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AutoOriginTLSKexEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[AutoOriginTLSKexEditResponse], ResultWrapper[AutoOriginTLSKexEditResponse]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoOriginTLSKexGetResponse:
        """
        When enabled, Cloudflare automatically selects the preferred TLS key-exchange
        algorithm to use when establishing the TLS connection to the zone's origin,
        picking from the algorithms permitted by the zone's
        `origin_tls_compliance_modes` setting. When disabled, the default key-exchange
        ordering is used.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            path_template("/zones/{zone_id}/settings/auto_origin_tls_kex", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AutoOriginTLSKexGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[AutoOriginTLSKexGetResponse], ResultWrapper[AutoOriginTLSKexGetResponse]),
        )


class AutoOriginTLSKexResourceWithRawResponse:
    def __init__(self, auto_origin_tls_kex: AutoOriginTLSKexResource) -> None:
        self._auto_origin_tls_kex = auto_origin_tls_kex

        self.edit = to_raw_response_wrapper(
            auto_origin_tls_kex.edit,
        )
        self.get = to_raw_response_wrapper(
            auto_origin_tls_kex.get,
        )


class AsyncAutoOriginTLSKexResourceWithRawResponse:
    def __init__(self, auto_origin_tls_kex: AsyncAutoOriginTLSKexResource) -> None:
        self._auto_origin_tls_kex = auto_origin_tls_kex

        self.edit = async_to_raw_response_wrapper(
            auto_origin_tls_kex.edit,
        )
        self.get = async_to_raw_response_wrapper(
            auto_origin_tls_kex.get,
        )


class AutoOriginTLSKexResourceWithStreamingResponse:
    def __init__(self, auto_origin_tls_kex: AutoOriginTLSKexResource) -> None:
        self._auto_origin_tls_kex = auto_origin_tls_kex

        self.edit = to_streamed_response_wrapper(
            auto_origin_tls_kex.edit,
        )
        self.get = to_streamed_response_wrapper(
            auto_origin_tls_kex.get,
        )


class AsyncAutoOriginTLSKexResourceWithStreamingResponse:
    def __init__(self, auto_origin_tls_kex: AsyncAutoOriginTLSKexResource) -> None:
        self._auto_origin_tls_kex = auto_origin_tls_kex

        self.edit = async_to_streamed_response_wrapper(
            auto_origin_tls_kex.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            auto_origin_tls_kex.get,
        )
