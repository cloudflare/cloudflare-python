# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .datasets import (
    Datasets,
    AsyncDatasets,
    DatasetsWithRawResponse,
    AsyncDatasetsWithRawResponse,
    DatasetsWithStreamingResponse,
    AsyncDatasetsWithStreamingResponse,
)
from .patterns import (
    Patterns,
    AsyncPatterns,
    PatternsWithRawResponse,
    AsyncPatternsWithRawResponse,
    PatternsWithStreamingResponse,
    AsyncPatternsWithStreamingResponse,
)
from .profiles import (
    Profiles,
    AsyncProfiles,
    ProfilesWithRawResponse,
    AsyncProfilesWithRawResponse,
    ProfilesWithStreamingResponse,
    AsyncProfilesWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .payload_logs import (
    PayloadLogs,
    AsyncPayloadLogs,
    PayloadLogsWithRawResponse,
    AsyncPayloadLogsWithRawResponse,
    PayloadLogsWithStreamingResponse,
    AsyncPayloadLogsWithStreamingResponse,
)
from .datasets.datasets import Datasets, AsyncDatasets
from .profiles.profiles import Profiles, AsyncProfiles

__all__ = ["DLP", "AsyncDLP"]


class DLP(SyncAPIResource):
    @cached_property
    def datasets(self) -> Datasets:
        return Datasets(self._client)

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
    def with_raw_response(self) -> DLPWithRawResponse:
        return DLPWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DLPWithStreamingResponse:
        return DLPWithStreamingResponse(self)


class AsyncDLP(AsyncAPIResource):
    @cached_property
    def datasets(self) -> AsyncDatasets:
        return AsyncDatasets(self._client)

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
    def with_raw_response(self) -> AsyncDLPWithRawResponse:
        return AsyncDLPWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDLPWithStreamingResponse:
        return AsyncDLPWithStreamingResponse(self)


class DLPWithRawResponse:
    def __init__(self, dlp: DLP) -> None:
        self._dlp = dlp

    @cached_property
    def datasets(self) -> DatasetsWithRawResponse:
        return DatasetsWithRawResponse(self._dlp.datasets)

    @cached_property
    def patterns(self) -> PatternsWithRawResponse:
        return PatternsWithRawResponse(self._dlp.patterns)

    @cached_property
    def payload_logs(self) -> PayloadLogsWithRawResponse:
        return PayloadLogsWithRawResponse(self._dlp.payload_logs)

    @cached_property
    def profiles(self) -> ProfilesWithRawResponse:
        return ProfilesWithRawResponse(self._dlp.profiles)


class AsyncDLPWithRawResponse:
    def __init__(self, dlp: AsyncDLP) -> None:
        self._dlp = dlp

    @cached_property
    def datasets(self) -> AsyncDatasetsWithRawResponse:
        return AsyncDatasetsWithRawResponse(self._dlp.datasets)

    @cached_property
    def patterns(self) -> AsyncPatternsWithRawResponse:
        return AsyncPatternsWithRawResponse(self._dlp.patterns)

    @cached_property
    def payload_logs(self) -> AsyncPayloadLogsWithRawResponse:
        return AsyncPayloadLogsWithRawResponse(self._dlp.payload_logs)

    @cached_property
    def profiles(self) -> AsyncProfilesWithRawResponse:
        return AsyncProfilesWithRawResponse(self._dlp.profiles)


class DLPWithStreamingResponse:
    def __init__(self, dlp: DLP) -> None:
        self._dlp = dlp

    @cached_property
    def datasets(self) -> DatasetsWithStreamingResponse:
        return DatasetsWithStreamingResponse(self._dlp.datasets)

    @cached_property
    def patterns(self) -> PatternsWithStreamingResponse:
        return PatternsWithStreamingResponse(self._dlp.patterns)

    @cached_property
    def payload_logs(self) -> PayloadLogsWithStreamingResponse:
        return PayloadLogsWithStreamingResponse(self._dlp.payload_logs)

    @cached_property
    def profiles(self) -> ProfilesWithStreamingResponse:
        return ProfilesWithStreamingResponse(self._dlp.profiles)


class AsyncDLPWithStreamingResponse:
    def __init__(self, dlp: AsyncDLP) -> None:
        self._dlp = dlp

    @cached_property
    def datasets(self) -> AsyncDatasetsWithStreamingResponse:
        return AsyncDatasetsWithStreamingResponse(self._dlp.datasets)

    @cached_property
    def patterns(self) -> AsyncPatternsWithStreamingResponse:
        return AsyncPatternsWithStreamingResponse(self._dlp.patterns)

    @cached_property
    def payload_logs(self) -> AsyncPayloadLogsWithStreamingResponse:
        return AsyncPayloadLogsWithStreamingResponse(self._dlp.payload_logs)

    @cached_property
    def profiles(self) -> AsyncProfilesWithStreamingResponse:
        return AsyncProfilesWithStreamingResponse(self._dlp.profiles)
