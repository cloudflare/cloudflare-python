# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .datasets.datasets import DatasetsResource, AsyncDatasetsResource

from ...._compat import cached_property

from .patterns import PatternsResource, AsyncPatternsResource

from .payload_logs import PayloadLogsResource, AsyncPayloadLogsResource

from .profiles.profiles import ProfilesResource, AsyncProfilesResource

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from .datasets import DatasetsResource, AsyncDatasetsResource, DatasetsResourceWithRawResponse, AsyncDatasetsResourceWithRawResponse, DatasetsResourceWithStreamingResponse, AsyncDatasetsResourceWithStreamingResponse
from .patterns import PatternsResource, AsyncPatternsResource, PatternsResourceWithRawResponse, AsyncPatternsResourceWithRawResponse, PatternsResourceWithStreamingResponse, AsyncPatternsResourceWithStreamingResponse
from .payload_logs import PayloadLogsResource, AsyncPayloadLogsResource, PayloadLogsResourceWithRawResponse, AsyncPayloadLogsResourceWithRawResponse, PayloadLogsResourceWithStreamingResponse, AsyncPayloadLogsResourceWithStreamingResponse
from .profiles import ProfilesResource, AsyncProfilesResource, ProfilesResourceWithRawResponse, AsyncProfilesResourceWithRawResponse, ProfilesResourceWithStreamingResponse, AsyncProfilesResourceWithStreamingResponse

__all__ = ["DLPResource", "AsyncDLPResource"]

class DLPResource(SyncAPIResource):
    @cached_property
    def datasets(self) -> DatasetsResource:
        return DatasetsResource(self._client)

    @cached_property
    def patterns(self) -> PatternsResource:
        return PatternsResource(self._client)

    @cached_property
    def payload_logs(self) -> PayloadLogsResource:
        return PayloadLogsResource(self._client)

    @cached_property
    def profiles(self) -> ProfilesResource:
        return ProfilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> DLPResourceWithRawResponse:
        return DLPResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DLPResourceWithStreamingResponse:
        return DLPResourceWithStreamingResponse(self)

class AsyncDLPResource(AsyncAPIResource):
    @cached_property
    def datasets(self) -> AsyncDatasetsResource:
        return AsyncDatasetsResource(self._client)

    @cached_property
    def patterns(self) -> AsyncPatternsResource:
        return AsyncPatternsResource(self._client)

    @cached_property
    def payload_logs(self) -> AsyncPayloadLogsResource:
        return AsyncPayloadLogsResource(self._client)

    @cached_property
    def profiles(self) -> AsyncProfilesResource:
        return AsyncProfilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDLPResourceWithRawResponse:
        return AsyncDLPResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDLPResourceWithStreamingResponse:
        return AsyncDLPResourceWithStreamingResponse(self)

class DLPResourceWithRawResponse:
    def __init__(self, dlp: DLPResource) -> None:
        self._dlp = dlp

    @cached_property
    def datasets(self) -> DatasetsResourceWithRawResponse:
        return DatasetsResourceWithRawResponse(self._dlp.datasets)

    @cached_property
    def patterns(self) -> PatternsResourceWithRawResponse:
        return PatternsResourceWithRawResponse(self._dlp.patterns)

    @cached_property
    def payload_logs(self) -> PayloadLogsResourceWithRawResponse:
        return PayloadLogsResourceWithRawResponse(self._dlp.payload_logs)

    @cached_property
    def profiles(self) -> ProfilesResourceWithRawResponse:
        return ProfilesResourceWithRawResponse(self._dlp.profiles)

class AsyncDLPResourceWithRawResponse:
    def __init__(self, dlp: AsyncDLPResource) -> None:
        self._dlp = dlp

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithRawResponse:
        return AsyncDatasetsResourceWithRawResponse(self._dlp.datasets)

    @cached_property
    def patterns(self) -> AsyncPatternsResourceWithRawResponse:
        return AsyncPatternsResourceWithRawResponse(self._dlp.patterns)

    @cached_property
    def payload_logs(self) -> AsyncPayloadLogsResourceWithRawResponse:
        return AsyncPayloadLogsResourceWithRawResponse(self._dlp.payload_logs)

    @cached_property
    def profiles(self) -> AsyncProfilesResourceWithRawResponse:
        return AsyncProfilesResourceWithRawResponse(self._dlp.profiles)

class DLPResourceWithStreamingResponse:
    def __init__(self, dlp: DLPResource) -> None:
        self._dlp = dlp

    @cached_property
    def datasets(self) -> DatasetsResourceWithStreamingResponse:
        return DatasetsResourceWithStreamingResponse(self._dlp.datasets)

    @cached_property
    def patterns(self) -> PatternsResourceWithStreamingResponse:
        return PatternsResourceWithStreamingResponse(self._dlp.patterns)

    @cached_property
    def payload_logs(self) -> PayloadLogsResourceWithStreamingResponse:
        return PayloadLogsResourceWithStreamingResponse(self._dlp.payload_logs)

    @cached_property
    def profiles(self) -> ProfilesResourceWithStreamingResponse:
        return ProfilesResourceWithStreamingResponse(self._dlp.profiles)

class AsyncDLPResourceWithStreamingResponse:
    def __init__(self, dlp: AsyncDLPResource) -> None:
        self._dlp = dlp

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithStreamingResponse:
        return AsyncDatasetsResourceWithStreamingResponse(self._dlp.datasets)

    @cached_property
    def patterns(self) -> AsyncPatternsResourceWithStreamingResponse:
        return AsyncPatternsResourceWithStreamingResponse(self._dlp.patterns)

    @cached_property
    def payload_logs(self) -> AsyncPayloadLogsResourceWithStreamingResponse:
        return AsyncPayloadLogsResourceWithStreamingResponse(self._dlp.payload_logs)

    @cached_property
    def profiles(self) -> AsyncProfilesResourceWithStreamingResponse:
        return AsyncProfilesResourceWithStreamingResponse(self._dlp.profiles)