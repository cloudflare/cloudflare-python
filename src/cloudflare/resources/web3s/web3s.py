# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .hostnames.hostnames import Hostnames, AsyncHostnames

from ..._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from .hostnames import (
    Hostnames,
    AsyncHostnames,
    HostnamesWithRawResponse,
    AsyncHostnamesWithRawResponse,
    HostnamesWithStreamingResponse,
    AsyncHostnamesWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["Web3s", "AsyncWeb3s"]


class Web3s(SyncAPIResource):
    @cached_property
    def hostnames(self) -> Hostnames:
        return Hostnames(self._client)

    @cached_property
    def with_raw_response(self) -> Web3sWithRawResponse:
        return Web3sWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> Web3sWithStreamingResponse:
        return Web3sWithStreamingResponse(self)


class AsyncWeb3s(AsyncAPIResource):
    @cached_property
    def hostnames(self) -> AsyncHostnames:
        return AsyncHostnames(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWeb3sWithRawResponse:
        return AsyncWeb3sWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWeb3sWithStreamingResponse:
        return AsyncWeb3sWithStreamingResponse(self)


class Web3sWithRawResponse:
    def __init__(self, web3s: Web3s) -> None:
        self._web3s = web3s

    @cached_property
    def hostnames(self) -> HostnamesWithRawResponse:
        return HostnamesWithRawResponse(self._web3s.hostnames)


class AsyncWeb3sWithRawResponse:
    def __init__(self, web3s: AsyncWeb3s) -> None:
        self._web3s = web3s

    @cached_property
    def hostnames(self) -> AsyncHostnamesWithRawResponse:
        return AsyncHostnamesWithRawResponse(self._web3s.hostnames)


class Web3sWithStreamingResponse:
    def __init__(self, web3s: Web3s) -> None:
        self._web3s = web3s

    @cached_property
    def hostnames(self) -> HostnamesWithStreamingResponse:
        return HostnamesWithStreamingResponse(self._web3s.hostnames)


class AsyncWeb3sWithStreamingResponse:
    def __init__(self, web3s: AsyncWeb3s) -> None:
        self._web3s = web3s

    @cached_property
    def hostnames(self) -> AsyncHostnamesWithStreamingResponse:
        return AsyncHostnamesWithStreamingResponse(self._web3s.hostnames)
