# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .indicator_feeds import IndicatorFeeds, AsyncIndicatorFeeds

from ..._compat import cached_property

from .sinkholes import Sinkholes, AsyncSinkholes

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
from .indicator_feeds import (
    IndicatorFeeds,
    AsyncIndicatorFeeds,
    IndicatorFeedsWithRawResponse,
    AsyncIndicatorFeedsWithRawResponse,
    IndicatorFeedsWithStreamingResponse,
    AsyncIndicatorFeedsWithStreamingResponse,
)
from .sinkholes import (
    Sinkholes,
    AsyncSinkholes,
    SinkholesWithRawResponse,
    AsyncSinkholesWithRawResponse,
    SinkholesWithStreamingResponse,
    AsyncSinkholesWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["Intel", "AsyncIntel"]


class Intel(SyncAPIResource):
    @cached_property
    def indicator_feeds(self) -> IndicatorFeeds:
        return IndicatorFeeds(self._client)

    @cached_property
    def sinkholes(self) -> Sinkholes:
        return Sinkholes(self._client)

    @cached_property
    def with_raw_response(self) -> IntelWithRawResponse:
        return IntelWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntelWithStreamingResponse:
        return IntelWithStreamingResponse(self)


class AsyncIntel(AsyncAPIResource):
    @cached_property
    def indicator_feeds(self) -> AsyncIndicatorFeeds:
        return AsyncIndicatorFeeds(self._client)

    @cached_property
    def sinkholes(self) -> AsyncSinkholes:
        return AsyncSinkholes(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIntelWithRawResponse:
        return AsyncIntelWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntelWithStreamingResponse:
        return AsyncIntelWithStreamingResponse(self)


class IntelWithRawResponse:
    def __init__(self, intel: Intel) -> None:
        self._intel = intel

    @cached_property
    def indicator_feeds(self) -> IndicatorFeedsWithRawResponse:
        return IndicatorFeedsWithRawResponse(self._intel.indicator_feeds)

    @cached_property
    def sinkholes(self) -> SinkholesWithRawResponse:
        return SinkholesWithRawResponse(self._intel.sinkholes)


class AsyncIntelWithRawResponse:
    def __init__(self, intel: AsyncIntel) -> None:
        self._intel = intel

    @cached_property
    def indicator_feeds(self) -> AsyncIndicatorFeedsWithRawResponse:
        return AsyncIndicatorFeedsWithRawResponse(self._intel.indicator_feeds)

    @cached_property
    def sinkholes(self) -> AsyncSinkholesWithRawResponse:
        return AsyncSinkholesWithRawResponse(self._intel.sinkholes)


class IntelWithStreamingResponse:
    def __init__(self, intel: Intel) -> None:
        self._intel = intel

    @cached_property
    def indicator_feeds(self) -> IndicatorFeedsWithStreamingResponse:
        return IndicatorFeedsWithStreamingResponse(self._intel.indicator_feeds)

    @cached_property
    def sinkholes(self) -> SinkholesWithStreamingResponse:
        return SinkholesWithStreamingResponse(self._intel.sinkholes)


class AsyncIntelWithStreamingResponse:
    def __init__(self, intel: AsyncIntel) -> None:
        self._intel = intel

    @cached_property
    def indicator_feeds(self) -> AsyncIndicatorFeedsWithStreamingResponse:
        return AsyncIndicatorFeedsWithStreamingResponse(self._intel.indicator_feeds)

    @cached_property
    def sinkholes(self) -> AsyncSinkholesWithStreamingResponse:
        return AsyncSinkholesWithStreamingResponse(self._intel.sinkholes)
