# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ....types.magics.ipsec_tunnels import PSKGenerateCreateResponse

__all__ = ["PSKGenerates", "AsyncPSKGenerates"]


class PSKGenerates(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PSKGeneratesWithRawResponse:
        return PSKGeneratesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PSKGeneratesWithStreamingResponse:
        return PSKGeneratesWithStreamingResponse(self)

    def create(
        self,
        tunnel_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PSKGenerateCreateResponse:
        """
        Generates a Pre Shared Key for a specific IPsec tunnel used in the IKE session.
        Use `?validate_only=true` as an optional query parameter to only run validation
        without persisting changes. After a PSK is generated, the PSK is immediately
        persisted to Cloudflare's edge and cannot be retrieved later. Note the PSK in a
        safe place.

        Args:
          account_identifier: Identifier

          tunnel_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not tunnel_identifier:
            raise ValueError(f"Expected a non-empty value for `tunnel_identifier` but received {tunnel_identifier!r}")
        return self._post(
            f"/accounts/{account_identifier}/magic/ipsec_tunnels/{tunnel_identifier}/psk_generate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PSKGenerateCreateResponse], ResultWrapper[PSKGenerateCreateResponse]),
        )


class AsyncPSKGenerates(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPSKGeneratesWithRawResponse:
        return AsyncPSKGeneratesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPSKGeneratesWithStreamingResponse:
        return AsyncPSKGeneratesWithStreamingResponse(self)

    async def create(
        self,
        tunnel_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PSKGenerateCreateResponse:
        """
        Generates a Pre Shared Key for a specific IPsec tunnel used in the IKE session.
        Use `?validate_only=true` as an optional query parameter to only run validation
        without persisting changes. After a PSK is generated, the PSK is immediately
        persisted to Cloudflare's edge and cannot be retrieved later. Note the PSK in a
        safe place.

        Args:
          account_identifier: Identifier

          tunnel_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not tunnel_identifier:
            raise ValueError(f"Expected a non-empty value for `tunnel_identifier` but received {tunnel_identifier!r}")
        return await self._post(
            f"/accounts/{account_identifier}/magic/ipsec_tunnels/{tunnel_identifier}/psk_generate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PSKGenerateCreateResponse], ResultWrapper[PSKGenerateCreateResponse]),
        )


class PSKGeneratesWithRawResponse:
    def __init__(self, psk_generates: PSKGenerates) -> None:
        self._psk_generates = psk_generates

        self.create = to_raw_response_wrapper(
            psk_generates.create,
        )


class AsyncPSKGeneratesWithRawResponse:
    def __init__(self, psk_generates: AsyncPSKGenerates) -> None:
        self._psk_generates = psk_generates

        self.create = async_to_raw_response_wrapper(
            psk_generates.create,
        )


class PSKGeneratesWithStreamingResponse:
    def __init__(self, psk_generates: PSKGenerates) -> None:
        self._psk_generates = psk_generates

        self.create = to_streamed_response_wrapper(
            psk_generates.create,
        )


class AsyncPSKGeneratesWithStreamingResponse:
    def __init__(self, psk_generates: AsyncPSKGenerates) -> None:
        self._psk_generates = psk_generates

        self.create = async_to_streamed_response_wrapper(
            psk_generates.create,
        )
