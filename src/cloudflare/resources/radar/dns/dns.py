# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .tops.tops import Tops, AsyncTops

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
from .tops import (
    Tops,
    AsyncTops,
    TopsWithRawResponse,
    AsyncTopsWithRawResponse,
    TopsWithStreamingResponse,
    AsyncTopsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper

__all__ = ["DNS", "AsyncDNS"]


class DNS(SyncAPIResource):
    @cached_property
    def tops(self) -> Tops:
        return Tops(self._client)

    @cached_property
    def with_raw_response(self) -> DNSWithRawResponse:
        return DNSWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DNSWithStreamingResponse:
        return DNSWithStreamingResponse(self)


class AsyncDNS(AsyncAPIResource):
    @cached_property
    def tops(self) -> AsyncTops:
        return AsyncTops(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDNSWithRawResponse:
        return AsyncDNSWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDNSWithStreamingResponse:
        return AsyncDNSWithStreamingResponse(self)


class DNSWithRawResponse:
    def __init__(self, dns: DNS) -> None:
        self._dns = dns

    @cached_property
    def tops(self) -> TopsWithRawResponse:
        return TopsWithRawResponse(self._dns.tops)


class AsyncDNSWithRawResponse:
    def __init__(self, dns: AsyncDNS) -> None:
        self._dns = dns

    @cached_property
    def tops(self) -> AsyncTopsWithRawResponse:
        return AsyncTopsWithRawResponse(self._dns.tops)


class DNSWithStreamingResponse:
    def __init__(self, dns: DNS) -> None:
        self._dns = dns

    @cached_property
    def tops(self) -> TopsWithStreamingResponse:
        return TopsWithStreamingResponse(self._dns.tops)


class AsyncDNSWithStreamingResponse:
    def __init__(self, dns: AsyncDNS) -> None:
        self._dns = dns

    @cached_property
    def tops(self) -> AsyncTopsWithStreamingResponse:
        return AsyncTopsWithStreamingResponse(self._dns.tops)
