# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .v3s.v3s import V3s, AsyncV3s

from ..._compat import cached_property

from .v3.v3 import V3, AsyncV3

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
from .v3s import (
    V3s,
    AsyncV3s,
    V3sWithRawResponse,
    AsyncV3sWithRawResponse,
    V3sWithStreamingResponse,
    AsyncV3sWithStreamingResponse,
)
from .v3 import (
    V3,
    AsyncV3,
    V3WithRawResponse,
    AsyncV3WithRawResponse,
    V3WithStreamingResponse,
    AsyncV3WithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["Alerting", "AsyncAlerting"]


class Alerting(SyncAPIResource):
    @cached_property
    def v3s(self) -> V3s:
        return V3s(self._client)

    @cached_property
    def v3(self) -> V3:
        return V3(self._client)

    @cached_property
    def with_raw_response(self) -> AlertingWithRawResponse:
        return AlertingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AlertingWithStreamingResponse:
        return AlertingWithStreamingResponse(self)


class AsyncAlerting(AsyncAPIResource):
    @cached_property
    def v3s(self) -> AsyncV3s:
        return AsyncV3s(self._client)

    @cached_property
    def v3(self) -> AsyncV3:
        return AsyncV3(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAlertingWithRawResponse:
        return AsyncAlertingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAlertingWithStreamingResponse:
        return AsyncAlertingWithStreamingResponse(self)


class AlertingWithRawResponse:
    def __init__(self, alerting: Alerting) -> None:
        self._alerting = alerting

    @cached_property
    def v3s(self) -> V3sWithRawResponse:
        return V3sWithRawResponse(self._alerting.v3s)

    @cached_property
    def v3(self) -> V3WithRawResponse:
        return V3WithRawResponse(self._alerting.v3)


class AsyncAlertingWithRawResponse:
    def __init__(self, alerting: AsyncAlerting) -> None:
        self._alerting = alerting

    @cached_property
    def v3s(self) -> AsyncV3sWithRawResponse:
        return AsyncV3sWithRawResponse(self._alerting.v3s)

    @cached_property
    def v3(self) -> AsyncV3WithRawResponse:
        return AsyncV3WithRawResponse(self._alerting.v3)


class AlertingWithStreamingResponse:
    def __init__(self, alerting: Alerting) -> None:
        self._alerting = alerting

    @cached_property
    def v3s(self) -> V3sWithStreamingResponse:
        return V3sWithStreamingResponse(self._alerting.v3s)

    @cached_property
    def v3(self) -> V3WithStreamingResponse:
        return V3WithStreamingResponse(self._alerting.v3)


class AsyncAlertingWithStreamingResponse:
    def __init__(self, alerting: AsyncAlerting) -> None:
        self._alerting = alerting

    @cached_property
    def v3s(self) -> AsyncV3sWithStreamingResponse:
        return AsyncV3sWithStreamingResponse(self._alerting.v3s)

    @cached_property
    def v3(self) -> AsyncV3WithStreamingResponse:
        return AsyncV3WithStreamingResponse(self._alerting.v3)
