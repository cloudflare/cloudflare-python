# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .analytics.analytics import AnalyticsResource, AsyncAnalyticsResource

from ..._compat import cached_property

from .apps import AppsResource, AsyncAppsResource

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from .analytics import AnalyticsResource, AsyncAnalyticsResource, AnalyticsResourceWithRawResponse, AsyncAnalyticsResourceWithRawResponse, AnalyticsResourceWithStreamingResponse, AsyncAnalyticsResourceWithStreamingResponse
from .apps import AppsResource, AsyncAppsResource, AppsResourceWithRawResponse, AsyncAppsResourceWithRawResponse, AppsResourceWithStreamingResponse, AsyncAppsResourceWithStreamingResponse

__all__ = ["SpectrumResource", "AsyncSpectrumResource"]

class SpectrumResource(SyncAPIResource):
    @cached_property
    def analytics(self) -> AnalyticsResource:
        return AnalyticsResource(self._client)

    @cached_property
    def apps(self) -> AppsResource:
        return AppsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SpectrumResourceWithRawResponse:
        return SpectrumResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpectrumResourceWithStreamingResponse:
        return SpectrumResourceWithStreamingResponse(self)

class AsyncSpectrumResource(AsyncAPIResource):
    @cached_property
    def analytics(self) -> AsyncAnalyticsResource:
        return AsyncAnalyticsResource(self._client)

    @cached_property
    def apps(self) -> AsyncAppsResource:
        return AsyncAppsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSpectrumResourceWithRawResponse:
        return AsyncSpectrumResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpectrumResourceWithStreamingResponse:
        return AsyncSpectrumResourceWithStreamingResponse(self)

class SpectrumResourceWithRawResponse:
    def __init__(self, spectrum: SpectrumResource) -> None:
        self._spectrum = spectrum

    @cached_property
    def analytics(self) -> AnalyticsResourceWithRawResponse:
        return AnalyticsResourceWithRawResponse(self._spectrum.analytics)

    @cached_property
    def apps(self) -> AppsResourceWithRawResponse:
        return AppsResourceWithRawResponse(self._spectrum.apps)

class AsyncSpectrumResourceWithRawResponse:
    def __init__(self, spectrum: AsyncSpectrumResource) -> None:
        self._spectrum = spectrum

    @cached_property
    def analytics(self) -> AsyncAnalyticsResourceWithRawResponse:
        return AsyncAnalyticsResourceWithRawResponse(self._spectrum.analytics)

    @cached_property
    def apps(self) -> AsyncAppsResourceWithRawResponse:
        return AsyncAppsResourceWithRawResponse(self._spectrum.apps)

class SpectrumResourceWithStreamingResponse:
    def __init__(self, spectrum: SpectrumResource) -> None:
        self._spectrum = spectrum

    @cached_property
    def analytics(self) -> AnalyticsResourceWithStreamingResponse:
        return AnalyticsResourceWithStreamingResponse(self._spectrum.analytics)

    @cached_property
    def apps(self) -> AppsResourceWithStreamingResponse:
        return AppsResourceWithStreamingResponse(self._spectrum.apps)

class AsyncSpectrumResourceWithStreamingResponse:
    def __init__(self, spectrum: AsyncSpectrumResource) -> None:
        self._spectrum = spectrum

    @cached_property
    def analytics(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        return AsyncAnalyticsResourceWithStreamingResponse(self._spectrum.analytics)

    @cached_property
    def apps(self) -> AsyncAppsResourceWithStreamingResponse:
        return AsyncAppsResourceWithStreamingResponse(self._spectrum.apps)