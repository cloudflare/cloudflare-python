# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .hostnames.hostnames import HostnamesResource, AsyncHostnamesResource

from ..._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from .hostnames import HostnamesResource, AsyncHostnamesResource, HostnamesResourceWithRawResponse, AsyncHostnamesResourceWithRawResponse, HostnamesResourceWithStreamingResponse, AsyncHostnamesResourceWithStreamingResponse

__all__ = ["Web3Resource", "AsyncWeb3Resource"]

class Web3Resource(SyncAPIResource):
    @cached_property
    def hostnames(self) -> HostnamesResource:
        return HostnamesResource(self._client)

    @cached_property
    def with_raw_response(self) -> Web3ResourceWithRawResponse:
        return Web3ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> Web3ResourceWithStreamingResponse:
        return Web3ResourceWithStreamingResponse(self)

class AsyncWeb3Resource(AsyncAPIResource):
    @cached_property
    def hostnames(self) -> AsyncHostnamesResource:
        return AsyncHostnamesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWeb3ResourceWithRawResponse:
        return AsyncWeb3ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWeb3ResourceWithStreamingResponse:
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