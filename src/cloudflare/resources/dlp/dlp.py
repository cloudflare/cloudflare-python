# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .datasets import (
    Datasets,
    AsyncDatasets,
    DatasetsWithRawResponse,
    AsyncDatasetsWithRawResponse,
    DatasetsWithStreamingResponse,
    AsyncDatasetsWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["DLP", "AsyncDLP"]


class DLP(SyncAPIResource):
    @cached_property
    def datasets(self) -> Datasets:
        return Datasets(self._client)

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


class AsyncDLPWithRawResponse:
    def __init__(self, dlp: AsyncDLP) -> None:
        self._dlp = dlp

    @cached_property
    def datasets(self) -> AsyncDatasetsWithRawResponse:
        return AsyncDatasetsWithRawResponse(self._dlp.datasets)


class DLPWithStreamingResponse:
    def __init__(self, dlp: DLP) -> None:
        self._dlp = dlp

    @cached_property
    def datasets(self) -> DatasetsWithStreamingResponse:
        return DatasetsWithStreamingResponse(self._dlp.datasets)


class AsyncDLPWithStreamingResponse:
    def __init__(self, dlp: AsyncDLP) -> None:
        self._dlp = dlp

    @cached_property
    def datasets(self) -> AsyncDatasetsWithStreamingResponse:
        return AsyncDatasetsWithStreamingResponse(self._dlp.datasets)
