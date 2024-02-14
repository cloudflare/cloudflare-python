# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .packages.packages import Packages, AsyncPackages

from ...._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from .packages import (
    Packages,
    AsyncPackages,
    PackagesWithRawResponse,
    AsyncPackagesWithRawResponse,
    PackagesWithStreamingResponse,
    AsyncPackagesWithStreamingResponse,
)
from ...._wrappers import ResultWrapper

__all__ = ["WAF", "AsyncWAF"]


class WAF(SyncAPIResource):
    @cached_property
    def packages(self) -> Packages:
        return Packages(self._client)

    @cached_property
    def with_raw_response(self) -> WAFWithRawResponse:
        return WAFWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WAFWithStreamingResponse:
        return WAFWithStreamingResponse(self)


class AsyncWAF(AsyncAPIResource):
    @cached_property
    def packages(self) -> AsyncPackages:
        return AsyncPackages(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWAFWithRawResponse:
        return AsyncWAFWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWAFWithStreamingResponse:
        return AsyncWAFWithStreamingResponse(self)


class WAFWithRawResponse:
    def __init__(self, waf: WAF) -> None:
        self._waf = waf

    @cached_property
    def packages(self) -> PackagesWithRawResponse:
        return PackagesWithRawResponse(self._waf.packages)


class AsyncWAFWithRawResponse:
    def __init__(self, waf: AsyncWAF) -> None:
        self._waf = waf

    @cached_property
    def packages(self) -> AsyncPackagesWithRawResponse:
        return AsyncPackagesWithRawResponse(self._waf.packages)


class WAFWithStreamingResponse:
    def __init__(self, waf: WAF) -> None:
        self._waf = waf

    @cached_property
    def packages(self) -> PackagesWithStreamingResponse:
        return PackagesWithStreamingResponse(self._waf.packages)


class AsyncWAFWithStreamingResponse:
    def __init__(self, waf: AsyncWAF) -> None:
        self._waf = waf

    @cached_property
    def packages(self) -> AsyncPackagesWithStreamingResponse:
        return AsyncPackagesWithStreamingResponse(self._waf.packages)
