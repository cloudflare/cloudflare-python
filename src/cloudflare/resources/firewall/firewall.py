# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .waf.waf import WAF, AsyncWAF

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
from .waf import (
    WAF,
    AsyncWAF,
    WAFWithRawResponse,
    AsyncWAFWithRawResponse,
    WAFWithStreamingResponse,
    AsyncWAFWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["Firewall", "AsyncFirewall"]


class Firewall(SyncAPIResource):
    @cached_property
    def waf(self) -> WAF:
        return WAF(self._client)

    @cached_property
    def with_raw_response(self) -> FirewallWithRawResponse:
        return FirewallWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FirewallWithStreamingResponse:
        return FirewallWithStreamingResponse(self)


class AsyncFirewall(AsyncAPIResource):
    @cached_property
    def waf(self) -> AsyncWAF:
        return AsyncWAF(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFirewallWithRawResponse:
        return AsyncFirewallWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFirewallWithStreamingResponse:
        return AsyncFirewallWithStreamingResponse(self)


class FirewallWithRawResponse:
    def __init__(self, firewall: Firewall) -> None:
        self._firewall = firewall

    @cached_property
    def waf(self) -> WAFWithRawResponse:
        return WAFWithRawResponse(self._firewall.waf)


class AsyncFirewallWithRawResponse:
    def __init__(self, firewall: AsyncFirewall) -> None:
        self._firewall = firewall

    @cached_property
    def waf(self) -> AsyncWAFWithRawResponse:
        return AsyncWAFWithRawResponse(self._firewall.waf)


class FirewallWithStreamingResponse:
    def __init__(self, firewall: Firewall) -> None:
        self._firewall = firewall

    @cached_property
    def waf(self) -> WAFWithStreamingResponse:
        return WAFWithStreamingResponse(self._firewall.waf)


class AsyncFirewallWithStreamingResponse:
    def __init__(self, firewall: AsyncFirewall) -> None:
        self._firewall = firewall

    @cached_property
    def waf(self) -> AsyncWAFWithStreamingResponse:
        return AsyncWAFWithStreamingResponse(self._firewall.waf)
