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
from ....types.zones.settings import ZonesTLSClientAuth, tls_client_auth_edit_params

__all__ = ["TLSClientAuth", "AsyncTLSClientAuth"]


class TLSClientAuth(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TLSClientAuthWithRawResponse:
        return TLSClientAuthWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TLSClientAuthWithStreamingResponse:
        return TLSClientAuthWithStreamingResponse(self)

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
    ) -> Optional[ZonesTLSClientAuth]:
        """
        TLS Client Auth requires Cloudflare to connect to your origin server using a
        client certificate (Enterprise Only).

        Args:
          zone_id: Identifier

          value: value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/tls_client_auth",
            body=maybe_transform({"value": value}, tls_client_auth_edit_params.TLSClientAuthEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesTLSClientAuth]], ResultWrapper[ZonesTLSClientAuth]),
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
    ) -> Optional[ZonesTLSClientAuth]:
        """
        TLS Client Auth requires Cloudflare to connect to your origin server using a
        client certificate (Enterprise Only).

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
            f"/zones/{zone_id}/settings/tls_client_auth",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesTLSClientAuth]], ResultWrapper[ZonesTLSClientAuth]),
        )


class AsyncTLSClientAuth(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTLSClientAuthWithRawResponse:
        return AsyncTLSClientAuthWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTLSClientAuthWithStreamingResponse:
        return AsyncTLSClientAuthWithStreamingResponse(self)

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
    ) -> Optional[ZonesTLSClientAuth]:
        """
        TLS Client Auth requires Cloudflare to connect to your origin server using a
        client certificate (Enterprise Only).

        Args:
          zone_id: Identifier

          value: value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/tls_client_auth",
            body=await async_maybe_transform({"value": value}, tls_client_auth_edit_params.TLSClientAuthEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesTLSClientAuth]], ResultWrapper[ZonesTLSClientAuth]),
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
    ) -> Optional[ZonesTLSClientAuth]:
        """
        TLS Client Auth requires Cloudflare to connect to your origin server using a
        client certificate (Enterprise Only).

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
            f"/zones/{zone_id}/settings/tls_client_auth",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesTLSClientAuth]], ResultWrapper[ZonesTLSClientAuth]),
        )


class TLSClientAuthWithRawResponse:
    def __init__(self, tls_client_auth: TLSClientAuth) -> None:
        self._tls_client_auth = tls_client_auth

        self.edit = to_raw_response_wrapper(
            tls_client_auth.edit,
        )
        self.get = to_raw_response_wrapper(
            tls_client_auth.get,
        )


class AsyncTLSClientAuthWithRawResponse:
    def __init__(self, tls_client_auth: AsyncTLSClientAuth) -> None:
        self._tls_client_auth = tls_client_auth

        self.edit = async_to_raw_response_wrapper(
            tls_client_auth.edit,
        )
        self.get = async_to_raw_response_wrapper(
            tls_client_auth.get,
        )


class TLSClientAuthWithStreamingResponse:
    def __init__(self, tls_client_auth: TLSClientAuth) -> None:
        self._tls_client_auth = tls_client_auth

        self.edit = to_streamed_response_wrapper(
            tls_client_auth.edit,
        )
        self.get = to_streamed_response_wrapper(
            tls_client_auth.get,
        )


class AsyncTLSClientAuthWithStreamingResponse:
    def __init__(self, tls_client_auth: AsyncTLSClientAuth) -> None:
        self._tls_client_auth = tls_client_auth

        self.edit = async_to_streamed_response_wrapper(
            tls_client_auth.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            tls_client_auth.get,
        )
