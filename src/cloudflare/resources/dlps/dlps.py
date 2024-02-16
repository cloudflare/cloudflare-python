# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .patterns.patterns import Patterns, AsyncPatterns

from ..._compat import cached_property

from .payload_logs import PayloadLogs, AsyncPayloadLogs

from .profiles.profiles import Profiles, AsyncProfiles

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
from .patterns import (
    Patterns,
    AsyncPatterns,
    PatternsWithRawResponse,
    AsyncPatternsWithRawResponse,
    PatternsWithStreamingResponse,
    AsyncPatternsWithStreamingResponse,
)
from .payload_logs import (
    PayloadLogs,
    AsyncPayloadLogs,
    PayloadLogsWithRawResponse,
    AsyncPayloadLogsWithRawResponse,
    PayloadLogsWithStreamingResponse,
    AsyncPayloadLogsWithStreamingResponse,
)
from .profiles import (
    Profiles,
    AsyncProfiles,
    ProfilesWithRawResponse,
    AsyncProfilesWithRawResponse,
    ProfilesWithStreamingResponse,
    AsyncProfilesWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["DLPs", "AsyncDLPs"]


class DLPs(SyncAPIResource):
    @cached_property
    def patterns(self) -> Patterns:
        return Patterns(self._client)

    @cached_property
    def payload_logs(self) -> PayloadLogs:
        return PayloadLogs(self._client)

    @cached_property
    def profiles(self) -> Profiles:
        return Profiles(self._client)

    @cached_property
    def with_raw_response(self) -> DLPsWithRawResponse:
        return DLPsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DLPsWithStreamingResponse:
        return DLPsWithStreamingResponse(self)


class AsyncDLPs(AsyncAPIResource):
    @cached_property
    def patterns(self) -> AsyncPatterns:
        return AsyncPatterns(self._client)

    @cached_property
    def payload_logs(self) -> AsyncPayloadLogs:
        return AsyncPayloadLogs(self._client)

    @cached_property
    def profiles(self) -> AsyncProfiles:
        return AsyncProfiles(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDLPsWithRawResponse:
        return AsyncDLPsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDLPsWithStreamingResponse:
        return AsyncDLPsWithStreamingResponse(self)


class DLPsWithRawResponse:
    def __init__(self, dlps: DLPs) -> None:
        self._dlps = dlps

    @cached_property
    def patterns(self) -> PatternsWithRawResponse:
        return PatternsWithRawResponse(self._dlps.patterns)

    @cached_property
    def payload_logs(self) -> PayloadLogsWithRawResponse:
        return PayloadLogsWithRawResponse(self._dlps.payload_logs)

    @cached_property
    def profiles(self) -> ProfilesWithRawResponse:
        return ProfilesWithRawResponse(self._dlps.profiles)


class AsyncDLPsWithRawResponse:
    def __init__(self, dlps: AsyncDLPs) -> None:
        self._dlps = dlps

    @cached_property
    def patterns(self) -> AsyncPatternsWithRawResponse:
        return AsyncPatternsWithRawResponse(self._dlps.patterns)

    @cached_property
    def payload_logs(self) -> AsyncPayloadLogsWithRawResponse:
        return AsyncPayloadLogsWithRawResponse(self._dlps.payload_logs)

    @cached_property
    def profiles(self) -> AsyncProfilesWithRawResponse:
        return AsyncProfilesWithRawResponse(self._dlps.profiles)


class DLPsWithStreamingResponse:
    def __init__(self, dlps: DLPs) -> None:
        self._dlps = dlps

    @cached_property
    def patterns(self) -> PatternsWithStreamingResponse:
        return PatternsWithStreamingResponse(self._dlps.patterns)

    @cached_property
    def payload_logs(self) -> PayloadLogsWithStreamingResponse:
        return PayloadLogsWithStreamingResponse(self._dlps.payload_logs)

    @cached_property
    def profiles(self) -> ProfilesWithStreamingResponse:
        return ProfilesWithStreamingResponse(self._dlps.profiles)


class AsyncDLPsWithStreamingResponse:
    def __init__(self, dlps: AsyncDLPs) -> None:
        self._dlps = dlps

    @cached_property
    def patterns(self) -> AsyncPatternsWithStreamingResponse:
        return AsyncPatternsWithStreamingResponse(self._dlps.patterns)

    @cached_property
    def payload_logs(self) -> AsyncPayloadLogsWithStreamingResponse:
        return AsyncPayloadLogsWithStreamingResponse(self._dlps.payload_logs)

    @cached_property
    def profiles(self) -> AsyncProfilesWithStreamingResponse:
        return AsyncProfilesWithStreamingResponse(self._dlps.profiles)
