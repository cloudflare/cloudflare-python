# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .jobs import (
    Jobs,
    AsyncJobs,
    JobsWithRawResponse,
    AsyncJobsWithRawResponse,
    JobsWithStreamingResponse,
    AsyncJobsWithStreamingResponse,
)
from .edges import (
    Edges,
    AsyncEdges,
    EdgesWithRawResponse,
    AsyncEdgesWithRawResponse,
    EdgesWithStreamingResponse,
    AsyncEdgesWithStreamingResponse,
)
from .datasets import (
    Datasets,
    AsyncDatasets,
    DatasetsWithRawResponse,
    AsyncDatasetsWithRawResponse,
    DatasetsWithStreamingResponse,
    AsyncDatasetsWithStreamingResponse,
)
from ..._compat import cached_property
from .validates import (
    Validates,
    AsyncValidates,
    ValidatesWithRawResponse,
    AsyncValidatesWithRawResponse,
    ValidatesWithStreamingResponse,
    AsyncValidatesWithStreamingResponse,
)
from .ownerships import (
    Ownerships,
    AsyncOwnerships,
    OwnershipsWithRawResponse,
    AsyncOwnershipsWithRawResponse,
    OwnershipsWithStreamingResponse,
    AsyncOwnershipsWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .datasets.datasets import Datasets, AsyncDatasets
from .validates.validates import Validates, AsyncValidates
from .ownerships.ownerships import Ownerships, AsyncOwnerships

__all__ = ["Logpush", "AsyncLogpush"]


class Logpush(SyncAPIResource):
    @cached_property
    def datasets(self) -> Datasets:
        return Datasets(self._client)

    @cached_property
    def edges(self) -> Edges:
        return Edges(self._client)

    @cached_property
    def jobs(self) -> Jobs:
        return Jobs(self._client)

    @cached_property
    def ownerships(self) -> Ownerships:
        return Ownerships(self._client)

    @cached_property
    def validates(self) -> Validates:
        return Validates(self._client)

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
    def edges(self) -> AsyncEdges:
        return AsyncEdges(self._client)

    @cached_property
    def jobs(self) -> AsyncJobs:
        return AsyncJobs(self._client)

    @cached_property
    def ownerships(self) -> AsyncOwnerships:
        return AsyncOwnerships(self._client)

    @cached_property
    def validates(self) -> AsyncValidates:
        return AsyncValidates(self._client)

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
    def edges(self) -> EdgesWithRawResponse:
        return EdgesWithRawResponse(self._logpush.edges)

    @cached_property
    def jobs(self) -> JobsWithRawResponse:
        return JobsWithRawResponse(self._logpush.jobs)

    @cached_property
    def ownerships(self) -> OwnershipsWithRawResponse:
        return OwnershipsWithRawResponse(self._logpush.ownerships)

    @cached_property
    def validates(self) -> ValidatesWithRawResponse:
        return ValidatesWithRawResponse(self._logpush.validates)


class AsyncLogpushWithRawResponse:
    def __init__(self, logpush: AsyncLogpush) -> None:
        self._logpush = logpush

    @cached_property
    def datasets(self) -> AsyncDatasetsWithRawResponse:
        return AsyncDatasetsWithRawResponse(self._logpush.datasets)

    @cached_property
    def edges(self) -> AsyncEdgesWithRawResponse:
        return AsyncEdgesWithRawResponse(self._logpush.edges)

    @cached_property
    def jobs(self) -> AsyncJobsWithRawResponse:
        return AsyncJobsWithRawResponse(self._logpush.jobs)

    @cached_property
    def ownerships(self) -> AsyncOwnershipsWithRawResponse:
        return AsyncOwnershipsWithRawResponse(self._logpush.ownerships)

    @cached_property
    def validates(self) -> AsyncValidatesWithRawResponse:
        return AsyncValidatesWithRawResponse(self._logpush.validates)


class LogpushWithStreamingResponse:
    def __init__(self, logpush: Logpush) -> None:
        self._logpush = logpush

    @cached_property
    def datasets(self) -> DatasetsWithStreamingResponse:
        return DatasetsWithStreamingResponse(self._logpush.datasets)

    @cached_property
    def edges(self) -> EdgesWithStreamingResponse:
        return EdgesWithStreamingResponse(self._logpush.edges)

    @cached_property
    def jobs(self) -> JobsWithStreamingResponse:
        return JobsWithStreamingResponse(self._logpush.jobs)

    @cached_property
    def ownerships(self) -> OwnershipsWithStreamingResponse:
        return OwnershipsWithStreamingResponse(self._logpush.ownerships)

    @cached_property
    def validates(self) -> ValidatesWithStreamingResponse:
        return ValidatesWithStreamingResponse(self._logpush.validates)


class AsyncLogpushWithStreamingResponse:
    def __init__(self, logpush: AsyncLogpush) -> None:
        self._logpush = logpush

    @cached_property
    def datasets(self) -> AsyncDatasetsWithStreamingResponse:
        return AsyncDatasetsWithStreamingResponse(self._logpush.datasets)

    @cached_property
    def edges(self) -> AsyncEdgesWithStreamingResponse:
        return AsyncEdgesWithStreamingResponse(self._logpush.edges)

    @cached_property
    def jobs(self) -> AsyncJobsWithStreamingResponse:
        return AsyncJobsWithStreamingResponse(self._logpush.jobs)

    @cached_property
    def ownerships(self) -> AsyncOwnershipsWithStreamingResponse:
        return AsyncOwnershipsWithStreamingResponse(self._logpush.ownerships)

    @cached_property
    def validates(self) -> AsyncValidatesWithStreamingResponse:
        return AsyncValidatesWithStreamingResponse(self._logpush.validates)
