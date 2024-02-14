# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .analytics.analytics import Analytics, AsyncAnalytics

from ..._compat import cached_property

from .apps import Apps, AsyncApps

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
from .analytics import (
    Analytics,
    AsyncAnalytics,
    AnalyticsWithRawResponse,
    AsyncAnalyticsWithRawResponse,
    AnalyticsWithStreamingResponse,
    AsyncAnalyticsWithStreamingResponse,
)
from .apps import (
    Apps,
    AsyncApps,
    AppsWithRawResponse,
    AsyncAppsWithRawResponse,
    AppsWithStreamingResponse,
    AsyncAppsWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["Spectrums", "AsyncSpectrums"]


class Spectrums(SyncAPIResource):
    @cached_property
    def analytics(self) -> Analytics:
        return Analytics(self._client)

    @cached_property
    def apps(self) -> Apps:
        return Apps(self._client)

    @cached_property
    def with_raw_response(self) -> SpectrumsWithRawResponse:
        return SpectrumsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpectrumsWithStreamingResponse:
        return SpectrumsWithStreamingResponse(self)


class AsyncSpectrums(AsyncAPIResource):
    @cached_property
    def analytics(self) -> AsyncAnalytics:
        return AsyncAnalytics(self._client)

    @cached_property
    def apps(self) -> AsyncApps:
        return AsyncApps(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSpectrumsWithRawResponse:
        return AsyncSpectrumsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpectrumsWithStreamingResponse:
        return AsyncSpectrumsWithStreamingResponse(self)


class SpectrumsWithRawResponse:
    def __init__(self, spectrums: Spectrums) -> None:
        self._spectrums = spectrums

    @cached_property
    def analytics(self) -> AnalyticsWithRawResponse:
        return AnalyticsWithRawResponse(self._spectrums.analytics)

    @cached_property
    def apps(self) -> AppsWithRawResponse:
        return AppsWithRawResponse(self._spectrums.apps)


class AsyncSpectrumsWithRawResponse:
    def __init__(self, spectrums: AsyncSpectrums) -> None:
        self._spectrums = spectrums

    @cached_property
    def analytics(self) -> AsyncAnalyticsWithRawResponse:
        return AsyncAnalyticsWithRawResponse(self._spectrums.analytics)

    @cached_property
    def apps(self) -> AsyncAppsWithRawResponse:
        return AsyncAppsWithRawResponse(self._spectrums.apps)


class SpectrumsWithStreamingResponse:
    def __init__(self, spectrums: Spectrums) -> None:
        self._spectrums = spectrums

    @cached_property
    def analytics(self) -> AnalyticsWithStreamingResponse:
        return AnalyticsWithStreamingResponse(self._spectrums.analytics)

    @cached_property
    def apps(self) -> AppsWithStreamingResponse:
        return AppsWithStreamingResponse(self._spectrums.apps)


class AsyncSpectrumsWithStreamingResponse:
    def __init__(self, spectrums: AsyncSpectrums) -> None:
        self._spectrums = spectrums

    @cached_property
    def analytics(self) -> AsyncAnalyticsWithStreamingResponse:
        return AsyncAnalyticsWithStreamingResponse(self._spectrums.analytics)

    @cached_property
    def apps(self) -> AsyncAppsWithStreamingResponse:
        return AsyncAppsWithStreamingResponse(self._spectrums.apps)
