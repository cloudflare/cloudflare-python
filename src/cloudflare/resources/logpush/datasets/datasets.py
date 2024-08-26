# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from .fields import (
    FieldsResource,
    AsyncFieldsResource,
    FieldsResourceWithRawResponse,
    AsyncFieldsResourceWithRawResponse,
    FieldsResourceWithStreamingResponse,
    AsyncFieldsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["DatasetsResource", "AsyncDatasetsResource"]


class DatasetsResource(SyncAPIResource):
    @cached_property
    def fields(self) -> FieldsResource:
        return FieldsResource(self._client)

    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DatasetsResourceWithRawResponse:
        return DatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetsResourceWithStreamingResponse:
        return DatasetsResourceWithStreamingResponse(self)


class AsyncDatasetsResource(AsyncAPIResource):
    @cached_property
    def fields(self) -> AsyncFieldsResource:
        return AsyncFieldsResource(self._client)

    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDatasetsResourceWithRawResponse:
        return AsyncDatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetsResourceWithStreamingResponse:
        return AsyncDatasetsResourceWithStreamingResponse(self)


class DatasetsResourceWithRawResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

    @cached_property
    def fields(self) -> FieldsResourceWithRawResponse:
        return FieldsResourceWithRawResponse(self._datasets.fields)

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._datasets.jobs)


class AsyncDatasetsResourceWithRawResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

    @cached_property
    def fields(self) -> AsyncFieldsResourceWithRawResponse:
        return AsyncFieldsResourceWithRawResponse(self._datasets.fields)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._datasets.jobs)


class DatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

    @cached_property
    def fields(self) -> FieldsResourceWithStreamingResponse:
        return FieldsResourceWithStreamingResponse(self._datasets.fields)

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._datasets.jobs)


class AsyncDatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

    @cached_property
    def fields(self) -> AsyncFieldsResourceWithStreamingResponse:
        return AsyncFieldsResourceWithStreamingResponse(self._datasets.fields)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._datasets.jobs)
