# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .total_tls import TotalTLS, AsyncTotalTLS

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
from .total_tls import (
    TotalTLS,
    AsyncTotalTLS,
    TotalTLSWithRawResponse,
    AsyncTotalTLSWithRawResponse,
    TotalTLSWithStreamingResponse,
    AsyncTotalTLSWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["Acms", "AsyncAcms"]


class Acms(SyncAPIResource):
    @cached_property
    def total_tls(self) -> TotalTLS:
        return TotalTLS(self._client)

    @cached_property
    def with_raw_response(self) -> AcmsWithRawResponse:
        return AcmsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AcmsWithStreamingResponse:
        return AcmsWithStreamingResponse(self)


class AsyncAcms(AsyncAPIResource):
    @cached_property
    def total_tls(self) -> AsyncTotalTLS:
        return AsyncTotalTLS(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAcmsWithRawResponse:
        return AsyncAcmsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAcmsWithStreamingResponse:
        return AsyncAcmsWithStreamingResponse(self)


class AcmsWithRawResponse:
    def __init__(self, acms: Acms) -> None:
        self._acms = acms

    @cached_property
    def total_tls(self) -> TotalTLSWithRawResponse:
        return TotalTLSWithRawResponse(self._acms.total_tls)


class AsyncAcmsWithRawResponse:
    def __init__(self, acms: AsyncAcms) -> None:
        self._acms = acms

    @cached_property
    def total_tls(self) -> AsyncTotalTLSWithRawResponse:
        return AsyncTotalTLSWithRawResponse(self._acms.total_tls)


class AcmsWithStreamingResponse:
    def __init__(self, acms: Acms) -> None:
        self._acms = acms

    @cached_property
    def total_tls(self) -> TotalTLSWithStreamingResponse:
        return TotalTLSWithStreamingResponse(self._acms.total_tls)


class AsyncAcmsWithStreamingResponse:
    def __init__(self, acms: AsyncAcms) -> None:
        self._acms = acms

    @cached_property
    def total_tls(self) -> AsyncTotalTLSWithStreamingResponse:
        return AsyncTotalTLSWithStreamingResponse(self._acms.total_tls)
