# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.radar.post_quantum import tls_support_params
from ....types.radar.post_quantum.tls_support_response import TLSSupportResponse

__all__ = ["TLSResource", "AsyncTLSResource"]


class TLSResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TLSResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TLSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TLSResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TLSResourceWithStreamingResponse(self)

    def support(
        self,
        *,
        host: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TLSSupportResponse:
        """
        Tests whether a hostname or IP address supports Post-Quantum (PQ) TLS key
        exchange. Returns information about the negotiated key exchange algorithm and
        whether it uses PQ cryptography.

        Args:
          host: Hostname or IP address to test for Post-Quantum TLS support, optionally with
              port (defaults to 443).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/post_quantum/tls/support",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"host": host}, tls_support_params.TLSSupportParams),
                post_parser=ResultWrapper[TLSSupportResponse]._unwrapper,
            ),
            cast_to=cast(Type[TLSSupportResponse], ResultWrapper[TLSSupportResponse]),
        )


class AsyncTLSResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTLSResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTLSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTLSResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTLSResourceWithStreamingResponse(self)

    async def support(
        self,
        *,
        host: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TLSSupportResponse:
        """
        Tests whether a hostname or IP address supports Post-Quantum (PQ) TLS key
        exchange. Returns information about the negotiated key exchange algorithm and
        whether it uses PQ cryptography.

        Args:
          host: Hostname or IP address to test for Post-Quantum TLS support, optionally with
              port (defaults to 443).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/post_quantum/tls/support",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"host": host}, tls_support_params.TLSSupportParams),
                post_parser=ResultWrapper[TLSSupportResponse]._unwrapper,
            ),
            cast_to=cast(Type[TLSSupportResponse], ResultWrapper[TLSSupportResponse]),
        )


class TLSResourceWithRawResponse:
    def __init__(self, tls: TLSResource) -> None:
        self._tls = tls

        self.support = to_raw_response_wrapper(
            tls.support,
        )


class AsyncTLSResourceWithRawResponse:
    def __init__(self, tls: AsyncTLSResource) -> None:
        self._tls = tls

        self.support = async_to_raw_response_wrapper(
            tls.support,
        )


class TLSResourceWithStreamingResponse:
    def __init__(self, tls: TLSResource) -> None:
        self._tls = tls

        self.support = to_streamed_response_wrapper(
            tls.support,
        )


class AsyncTLSResourceWithStreamingResponse:
    def __init__(self, tls: AsyncTLSResource) -> None:
        self._tls = tls

        self.support = async_to_streamed_response_wrapper(
            tls.support,
        )
