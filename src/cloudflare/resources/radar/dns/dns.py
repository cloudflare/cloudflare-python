# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .top import TopResource, AsyncTopResource

from ...._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from .top import (
    TopResource,
    AsyncTopResource,
    TopResourceWithRawResponse,
    AsyncTopResourceWithRawResponse,
    TopResourceWithStreamingResponse,
    AsyncTopResourceWithStreamingResponse,
)

__all__ = ["DNSResource", "AsyncDNSResource"]


class DNSResource(SyncAPIResource):
    @cached_property
    def top(self) -> TopResource:
        return TopResource(self._client)

    @cached_property
    def with_raw_response(self) -> DNSResourceWithRawResponse:
        return DNSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DNSResourceWithStreamingResponse:
        return DNSResourceWithStreamingResponse(self)


class AsyncDNSResource(AsyncAPIResource):
    @cached_property
    def top(self) -> AsyncTopResource:
        return AsyncTopResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDNSResourceWithRawResponse:
        return AsyncDNSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDNSResourceWithStreamingResponse:
        return AsyncDNSResourceWithStreamingResponse(self)


class DNSResourceWithRawResponse:
    def __init__(self, dns: DNSResource) -> None:
        self._dns = dns

    @cached_property
    def top(self) -> TopResourceWithRawResponse:
        return TopResourceWithRawResponse(self._dns.top)


class AsyncDNSResourceWithRawResponse:
    def __init__(self, dns: AsyncDNSResource) -> None:
        self._dns = dns

    @cached_property
    def top(self) -> AsyncTopResourceWithRawResponse:
        return AsyncTopResourceWithRawResponse(self._dns.top)


class DNSResourceWithStreamingResponse:
    def __init__(self, dns: DNSResource) -> None:
        self._dns = dns

    @cached_property
    def top(self) -> TopResourceWithStreamingResponse:
        return TopResourceWithStreamingResponse(self._dns.top)


class AsyncDNSResourceWithStreamingResponse:
    def __init__(self, dns: AsyncDNSResource) -> None:
        self._dns = dns

    @cached_property
    def top(self) -> AsyncTopResourceWithStreamingResponse:
        return AsyncTopResourceWithStreamingResponse(self._dns.top)
