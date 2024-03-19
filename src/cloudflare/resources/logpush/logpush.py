# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .edge import (
    Edge,
    AsyncEdge,
    EdgeWithRawResponse,
    AsyncEdgeWithRawResponse,
    EdgeWithStreamingResponse,
    AsyncEdgeWithStreamingResponse,
)
from .jobs import (
    Jobs,
    AsyncJobs,
    JobsWithRawResponse,
    AsyncJobsWithRawResponse,
    JobsWithStreamingResponse,
    AsyncJobsWithStreamingResponse,
)
from .datasets import (
    Datasets,
    AsyncDatasets,
    DatasetsWithRawResponse,
    AsyncDatasetsWithRawResponse,
    DatasetsWithStreamingResponse,
    AsyncDatasetsWithStreamingResponse,
)
from .validate import (
    Validate,
    AsyncValidate,
    ValidateWithRawResponse,
    AsyncValidateWithRawResponse,
    ValidateWithStreamingResponse,
    AsyncValidateWithStreamingResponse,
)
from ..._compat import cached_property
from .ownership import (
    Ownership,
    AsyncOwnership,
    OwnershipWithRawResponse,
    AsyncOwnershipWithRawResponse,
    OwnershipWithStreamingResponse,
    AsyncOwnershipWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .datasets.datasets import Datasets, AsyncDatasets

__all__ = ["Logpush", "AsyncLogpush"]


class Logpush(SyncAPIResource):
    @cached_property
    def datasets(self) -> Datasets:
        return Datasets(self._client)

    @cached_property
    def edge(self) -> Edge:
        return Edge(self._client)

    @cached_property
    def jobs(self) -> Jobs:
        return Jobs(self._client)

    @cached_property
    def ownership(self) -> Ownership:
        return Ownership(self._client)

    @cached_property
    def validate(self) -> Validate:
        return Validate(self._client)

    @cached_property
    def with_raw_response(self) -> LogpushWithRawResponse:
        return LogpushWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogpushWithStreamingResponse:
        return LogpushWithStreamingResponse(self)


class AsyncLogpush(AsyncAPIResource):
    @cached_property
    def datasets(self) -> AsyncDatasets:
        return AsyncDatasets(self._client)

    @cached_property
    def edge(self) -> AsyncEdge:
        return AsyncEdge(self._client)

    @cached_property
    def jobs(self) -> AsyncJobs:
        return AsyncJobs(self._client)

    @cached_property
    def ownership(self) -> AsyncOwnership:
        return AsyncOwnership(self._client)

    @cached_property
    def validate(self) -> AsyncValidate:
        return AsyncValidate(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLogpushWithRawResponse:
        return AsyncLogpushWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogpushWithStreamingResponse:
        return AsyncLogpushWithStreamingResponse(self)


class LogpushWithRawResponse:
    def __init__(self, logpush: Logpush) -> None:
        self._logpush = logpush

    @cached_property
    def datasets(self) -> DatasetsWithRawResponse:
        return DatasetsWithRawResponse(self._logpush.datasets)

    @cached_property
    def edge(self) -> EdgeWithRawResponse:
        return EdgeWithRawResponse(self._logpush.edge)

    @cached_property
    def jobs(self) -> JobsWithRawResponse:
        return JobsWithRawResponse(self._logpush.jobs)

    @cached_property
    def ownership(self) -> OwnershipWithRawResponse:
        return OwnershipWithRawResponse(self._logpush.ownership)

    @cached_property
    def validate(self) -> ValidateWithRawResponse:
        return ValidateWithRawResponse(self._logpush.validate)


class AsyncLogpushWithRawResponse:
    def __init__(self, logpush: AsyncLogpush) -> None:
        self._logpush = logpush

    @cached_property
    def datasets(self) -> AsyncDatasetsWithRawResponse:
        return AsyncDatasetsWithRawResponse(self._logpush.datasets)

    @cached_property
    def edge(self) -> AsyncEdgeWithRawResponse:
        return AsyncEdgeWithRawResponse(self._logpush.edge)

    @cached_property
    def jobs(self) -> AsyncJobsWithRawResponse:
        return AsyncJobsWithRawResponse(self._logpush.jobs)

    @cached_property
    def ownership(self) -> AsyncOwnershipWithRawResponse:
        return AsyncOwnershipWithRawResponse(self._logpush.ownership)

    @cached_property
    def validate(self) -> AsyncValidateWithRawResponse:
        return AsyncValidateWithRawResponse(self._logpush.validate)


class LogpushWithStreamingResponse:
    def __init__(self, logpush: Logpush) -> None:
        self._logpush = logpush

    @cached_property
    def datasets(self) -> DatasetsWithStreamingResponse:
        return DatasetsWithStreamingResponse(self._logpush.datasets)

    @cached_property
    def edge(self) -> EdgeWithStreamingResponse:
        return EdgeWithStreamingResponse(self._logpush.edge)

    @cached_property
    def jobs(self) -> JobsWithStreamingResponse:
        return JobsWithStreamingResponse(self._logpush.jobs)

    @cached_property
    def ownership(self) -> OwnershipWithStreamingResponse:
        return OwnershipWithStreamingResponse(self._logpush.ownership)

    @cached_property
    def validate(self) -> ValidateWithStreamingResponse:
        return ValidateWithStreamingResponse(self._logpush.validate)


class AsyncLogpushWithStreamingResponse:
    def __init__(self, logpush: AsyncLogpush) -> None:
        self._logpush = logpush

    @cached_property
    def datasets(self) -> AsyncDatasetsWithStreamingResponse:
        return AsyncDatasetsWithStreamingResponse(self._logpush.datasets)

    @cached_property
    def edge(self) -> AsyncEdgeWithStreamingResponse:
        return AsyncEdgeWithStreamingResponse(self._logpush.edge)

    @cached_property
    def jobs(self) -> AsyncJobsWithStreamingResponse:
        return AsyncJobsWithStreamingResponse(self._logpush.jobs)

    @cached_property
    def ownership(self) -> AsyncOwnershipWithStreamingResponse:
        return AsyncOwnershipWithStreamingResponse(self._logpush.ownership)

    @cached_property
    def validate(self) -> AsyncValidateWithStreamingResponse:
        return AsyncValidateWithStreamingResponse(self._logpush.validate)
