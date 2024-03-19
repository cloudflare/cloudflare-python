# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .jobs import (
    Jobs,
    AsyncJobs,
    JobsWithRawResponse,
    AsyncJobsWithRawResponse,
    JobsWithStreamingResponse,
    AsyncJobsWithStreamingResponse,
)
from .fields import (
    Fields,
    AsyncFields,
    FieldsWithRawResponse,
    AsyncFieldsWithRawResponse,
    FieldsWithStreamingResponse,
    AsyncFieldsWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Datasets", "AsyncDatasets"]


class Datasets(SyncAPIResource):
    @cached_property
    def fields(self) -> Fields:
        return Fields(self._client)

    @cached_property
    def jobs(self) -> Jobs:
        return Jobs(self._client)

    @cached_property
    def with_raw_response(self) -> DatasetsWithRawResponse:
        return DatasetsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetsWithStreamingResponse:
        return DatasetsWithStreamingResponse(self)


class AsyncDatasets(AsyncAPIResource):
    @cached_property
    def fields(self) -> AsyncFields:
        return AsyncFields(self._client)

    @cached_property
    def jobs(self) -> AsyncJobs:
        return AsyncJobs(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDatasetsWithRawResponse:
        return AsyncDatasetsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetsWithStreamingResponse:
        return AsyncDatasetsWithStreamingResponse(self)


class DatasetsWithRawResponse:
    def __init__(self, datasets: Datasets) -> None:
        self._datasets = datasets

    @cached_property
    def fields(self) -> FieldsWithRawResponse:
        return FieldsWithRawResponse(self._datasets.fields)

    @cached_property
    def jobs(self) -> JobsWithRawResponse:
        return JobsWithRawResponse(self._datasets.jobs)


class AsyncDatasetsWithRawResponse:
    def __init__(self, datasets: AsyncDatasets) -> None:
        self._datasets = datasets

    @cached_property
    def fields(self) -> AsyncFieldsWithRawResponse:
        return AsyncFieldsWithRawResponse(self._datasets.fields)

    @cached_property
    def jobs(self) -> AsyncJobsWithRawResponse:
        return AsyncJobsWithRawResponse(self._datasets.jobs)


class DatasetsWithStreamingResponse:
    def __init__(self, datasets: Datasets) -> None:
        self._datasets = datasets

    @cached_property
    def fields(self) -> FieldsWithStreamingResponse:
        return FieldsWithStreamingResponse(self._datasets.fields)

    @cached_property
    def jobs(self) -> JobsWithStreamingResponse:
        return JobsWithStreamingResponse(self._datasets.jobs)


class AsyncDatasetsWithStreamingResponse:
    def __init__(self, datasets: AsyncDatasets) -> None:
        self._datasets = datasets

    @cached_property
    def fields(self) -> AsyncFieldsWithStreamingResponse:
        return AsyncFieldsWithStreamingResponse(self._datasets.fields)

    @cached_property
    def jobs(self) -> AsyncJobsWithStreamingResponse:
        return AsyncJobsWithStreamingResponse(self._datasets.jobs)
