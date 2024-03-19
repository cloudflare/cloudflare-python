# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .hostnames import (
    Hostnames,
    AsyncHostnames,
    HostnamesWithRawResponse,
    AsyncHostnamesWithRawResponse,
    HostnamesWithStreamingResponse,
    AsyncHostnamesWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .hostnames.hostnames import Hostnames, AsyncHostnames

__all__ = ["Web3", "AsyncWeb3"]


class Web3(SyncAPIResource):
    @cached_property
    def hostnames(self) -> Hostnames:
        return Hostnames(self._client)

    @cached_property
    def with_raw_response(self) -> Web3WithRawResponse:
        return Web3WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> Web3WithStreamingResponse:
        return Web3WithStreamingResponse(self)


class AsyncWeb3(AsyncAPIResource):
    @cached_property
    def hostnames(self) -> AsyncHostnames:
        return AsyncHostnames(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWeb3WithRawResponse:
        return AsyncWeb3WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWeb3WithStreamingResponse:
        return AsyncWeb3WithStreamingResponse(self)


class Web3WithRawResponse:
    def __init__(self, web3: Web3) -> None:
        self._web3 = web3

    @cached_property
    def hostnames(self) -> HostnamesWithRawResponse:
        return HostnamesWithRawResponse(self._web3.hostnames)


class AsyncWeb3WithRawResponse:
    def __init__(self, web3: AsyncWeb3) -> None:
        self._web3 = web3

    @cached_property
    def hostnames(self) -> AsyncHostnamesWithRawResponse:
        return AsyncHostnamesWithRawResponse(self._web3.hostnames)


class Web3WithStreamingResponse:
    def __init__(self, web3: Web3) -> None:
        self._web3 = web3

    @cached_property
    def hostnames(self) -> HostnamesWithStreamingResponse:
        return HostnamesWithStreamingResponse(self._web3.hostnames)


class AsyncWeb3WithStreamingResponse:
    def __init__(self, web3: AsyncWeb3) -> None:
        self._web3 = web3

    @cached_property
    def hostnames(self) -> AsyncHostnamesWithStreamingResponse:
        return AsyncHostnamesWithStreamingResponse(self._web3.hostnames)
