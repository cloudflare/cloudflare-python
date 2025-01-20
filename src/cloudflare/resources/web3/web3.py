# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .hostnames.hostnames import (
    HostnamesResource,
    AsyncHostnamesResource,
    HostnamesResourceWithRawResponse,
    AsyncHostnamesResourceWithRawResponse,
    HostnamesResourceWithStreamingResponse,
    AsyncHostnamesResourceWithStreamingResponse,
)

__all__ = ["Web3Resource", "AsyncWeb3Resource"]


class Web3Resource(SyncAPIResource):
    @cached_property
    def hostnames(self) -> HostnamesResource:
        return HostnamesResource(self._client)

    @cached_property
    def with_raw_response(self) -> Web3ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return Web3ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> Web3ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return Web3ResourceWithStreamingResponse(self)


class AsyncWeb3Resource(AsyncAPIResource):
    @cached_property
    def hostnames(self) -> AsyncHostnamesResource:
        return AsyncHostnamesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWeb3ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWeb3ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWeb3ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncWeb3ResourceWithStreamingResponse(self)


class Web3ResourceWithRawResponse:
    def __init__(self, web3: Web3Resource) -> None:
        self._web3 = web3

    @cached_property
    def hostnames(self) -> HostnamesResourceWithRawResponse:
        return HostnamesResourceWithRawResponse(self._web3.hostnames)


class AsyncWeb3ResourceWithRawResponse:
    def __init__(self, web3: AsyncWeb3Resource) -> None:
        self._web3 = web3

    @cached_property
    def hostnames(self) -> AsyncHostnamesResourceWithRawResponse:
        return AsyncHostnamesResourceWithRawResponse(self._web3.hostnames)


class Web3ResourceWithStreamingResponse:
    def __init__(self, web3: Web3Resource) -> None:
        self._web3 = web3

    @cached_property
    def hostnames(self) -> HostnamesResourceWithStreamingResponse:
        return HostnamesResourceWithStreamingResponse(self._web3.hostnames)


class AsyncWeb3ResourceWithStreamingResponse:
    def __init__(self, web3: AsyncWeb3Resource) -> None:
        self._web3 = web3

    @cached_property
    def hostnames(self) -> AsyncHostnamesResourceWithStreamingResponse:
        return AsyncHostnamesResourceWithStreamingResponse(self._web3.hostnames)
