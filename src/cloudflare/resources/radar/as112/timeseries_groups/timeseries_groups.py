# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .dnssec import DNSSEC, AsyncDNSSEC

from ....._compat import cached_property

from .edns import Edns, AsyncEdns

from .ip_version import IPVersion, AsyncIPVersion

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from .....types import shared_params
from .dnssec import (
    DNSSEC,
    AsyncDNSSEC,
    DNSSECWithRawResponse,
    AsyncDNSSECWithRawResponse,
    DNSSECWithStreamingResponse,
    AsyncDNSSECWithStreamingResponse,
)
from .edns import (
    Edns,
    AsyncEdns,
    EdnsWithRawResponse,
    AsyncEdnsWithRawResponse,
    EdnsWithStreamingResponse,
    AsyncEdnsWithStreamingResponse,
)
from .ip_version import (
    IPVersion,
    AsyncIPVersion,
    IPVersionWithRawResponse,
    AsyncIPVersionWithRawResponse,
    IPVersionWithStreamingResponse,
    AsyncIPVersionWithStreamingResponse,
)
from ....._wrappers import ResultWrapper

__all__ = ["TimeseriesGroups", "AsyncTimeseriesGroups"]


class TimeseriesGroups(SyncAPIResource):
    @cached_property
    def dnssec(self) -> DNSSEC:
        return DNSSEC(self._client)

    @cached_property
    def edns(self) -> Edns:
        return Edns(self._client)

    @cached_property
    def ip_version(self) -> IPVersion:
        return IPVersion(self._client)

    @cached_property
    def with_raw_response(self) -> TimeseriesGroupsWithRawResponse:
        return TimeseriesGroupsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TimeseriesGroupsWithStreamingResponse:
        return TimeseriesGroupsWithStreamingResponse(self)


class AsyncTimeseriesGroups(AsyncAPIResource):
    @cached_property
    def dnssec(self) -> AsyncDNSSEC:
        return AsyncDNSSEC(self._client)

    @cached_property
    def edns(self) -> AsyncEdns:
        return AsyncEdns(self._client)

    @cached_property
    def ip_version(self) -> AsyncIPVersion:
        return AsyncIPVersion(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTimeseriesGroupsWithRawResponse:
        return AsyncTimeseriesGroupsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTimeseriesGroupsWithStreamingResponse:
        return AsyncTimeseriesGroupsWithStreamingResponse(self)


class TimeseriesGroupsWithRawResponse:
    def __init__(self, timeseries_groups: TimeseriesGroups) -> None:
        self._timeseries_groups = timeseries_groups

    @cached_property
    def dnssec(self) -> DNSSECWithRawResponse:
        return DNSSECWithRawResponse(self._timeseries_groups.dnssec)

    @cached_property
    def edns(self) -> EdnsWithRawResponse:
        return EdnsWithRawResponse(self._timeseries_groups.edns)

    @cached_property
    def ip_version(self) -> IPVersionWithRawResponse:
        return IPVersionWithRawResponse(self._timeseries_groups.ip_version)


class AsyncTimeseriesGroupsWithRawResponse:
    def __init__(self, timeseries_groups: AsyncTimeseriesGroups) -> None:
        self._timeseries_groups = timeseries_groups

    @cached_property
    def dnssec(self) -> AsyncDNSSECWithRawResponse:
        return AsyncDNSSECWithRawResponse(self._timeseries_groups.dnssec)

    @cached_property
    def edns(self) -> AsyncEdnsWithRawResponse:
        return AsyncEdnsWithRawResponse(self._timeseries_groups.edns)

    @cached_property
    def ip_version(self) -> AsyncIPVersionWithRawResponse:
        return AsyncIPVersionWithRawResponse(self._timeseries_groups.ip_version)


class TimeseriesGroupsWithStreamingResponse:
    def __init__(self, timeseries_groups: TimeseriesGroups) -> None:
        self._timeseries_groups = timeseries_groups

    @cached_property
    def dnssec(self) -> DNSSECWithStreamingResponse:
        return DNSSECWithStreamingResponse(self._timeseries_groups.dnssec)

    @cached_property
    def edns(self) -> EdnsWithStreamingResponse:
        return EdnsWithStreamingResponse(self._timeseries_groups.edns)

    @cached_property
    def ip_version(self) -> IPVersionWithStreamingResponse:
        return IPVersionWithStreamingResponse(self._timeseries_groups.ip_version)


class AsyncTimeseriesGroupsWithStreamingResponse:
    def __init__(self, timeseries_groups: AsyncTimeseriesGroups) -> None:
        self._timeseries_groups = timeseries_groups

    @cached_property
    def dnssec(self) -> AsyncDNSSECWithStreamingResponse:
        return AsyncDNSSECWithStreamingResponse(self._timeseries_groups.dnssec)

    @cached_property
    def edns(self) -> AsyncEdnsWithStreamingResponse:
        return AsyncEdnsWithStreamingResponse(self._timeseries_groups.edns)

    @cached_property
    def ip_version(self) -> AsyncIPVersionWithStreamingResponse:
        return AsyncIPVersionWithStreamingResponse(self._timeseries_groups.ip_version)
