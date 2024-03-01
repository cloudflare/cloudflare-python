# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, cast

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
from ....types.zero_trust.tunnels import TokenGetResponse

__all__ = ["Token", "AsyncToken"]


class Token(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TokenWithRawResponse:
        return TokenWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TokenWithStreamingResponse:
        return TokenWithStreamingResponse(self)

    def get(
        self,
        tunnel_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenGetResponse:
        """
        Gets the token used to associate cloudflared with a specific tunnel.

        Args:
          account_id: Cloudflare account ID

          tunnel_id: UUID of the tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return cast(
            TokenGetResponse,
            self._get(
                f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}/token",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[TokenGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncToken(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTokenWithRawResponse:
        return AsyncTokenWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTokenWithStreamingResponse:
        return AsyncTokenWithStreamingResponse(self)

    async def get(
        self,
        tunnel_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenGetResponse:
        """
        Gets the token used to associate cloudflared with a specific tunnel.

        Args:
          account_id: Cloudflare account ID

          tunnel_id: UUID of the tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return cast(
            TokenGetResponse,
            await self._get(
                f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}/token",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[TokenGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class TokenWithRawResponse:
    def __init__(self, token: Token) -> None:
        self._token = token

        self.get = to_raw_response_wrapper(
            token.get,
        )


class AsyncTokenWithRawResponse:
    def __init__(self, token: AsyncToken) -> None:
        self._token = token

        self.get = async_to_raw_response_wrapper(
            token.get,
        )


class TokenWithStreamingResponse:
    def __init__(self, token: Token) -> None:
        self._token = token

        self.get = to_streamed_response_wrapper(
            token.get,
        )


class AsyncTokenWithStreamingResponse:
    def __init__(self, token: AsyncToken) -> None:
        self._token = token

        self.get = async_to_streamed_response_wrapper(
            token.get,
        )
