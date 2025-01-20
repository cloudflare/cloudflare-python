# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .edge import (
    EdgeResource,
    AsyncEdgeResource,
    EdgeResourceWithRawResponse,
    AsyncEdgeResourceWithRawResponse,
    EdgeResourceWithStreamingResponse,
    AsyncEdgeResourceWithStreamingResponse,
)
from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from .validate import (
    ValidateResource,
    AsyncValidateResource,
    ValidateResourceWithRawResponse,
    AsyncValidateResourceWithRawResponse,
    ValidateResourceWithStreamingResponse,
    AsyncValidateResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .ownership import (
    OwnershipResource,
    AsyncOwnershipResource,
    OwnershipResourceWithRawResponse,
    AsyncOwnershipResourceWithRawResponse,
    OwnershipResourceWithStreamingResponse,
    AsyncOwnershipResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .datasets.datasets import (
    DatasetsResource,
    AsyncDatasetsResource,
    DatasetsResourceWithRawResponse,
    AsyncDatasetsResourceWithRawResponse,
    DatasetsResourceWithStreamingResponse,
    AsyncDatasetsResourceWithStreamingResponse,
)

__all__ = ["LogpushResource", "AsyncLogpushResource"]


class LogpushResource(SyncAPIResource):
    @cached_property
    def datasets(self) -> DatasetsResource:
        return DatasetsResource(self._client)

    @cached_property
    def edge(self) -> EdgeResource:
        return EdgeResource(self._client)

    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def ownership(self) -> OwnershipResource:
        return OwnershipResource(self._client)

    @cached_property
    def validate(self) -> ValidateResource:
        return ValidateResource(self._client)

    @cached_property
    def with_raw_response(self) -> LogpushResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return LogpushResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogpushResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return LogpushResourceWithStreamingResponse(self)


class AsyncLogpushResource(AsyncAPIResource):
    @cached_property
    def datasets(self) -> AsyncDatasetsResource:
        return AsyncDatasetsResource(self._client)

    @cached_property
    def edge(self) -> AsyncEdgeResource:
        return AsyncEdgeResource(self._client)

    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def ownership(self) -> AsyncOwnershipResource:
        return AsyncOwnershipResource(self._client)

    @cached_property
    def validate(self) -> AsyncValidateResource:
        return AsyncValidateResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLogpushResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLogpushResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogpushResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncLogpushResourceWithStreamingResponse(self)


class LogpushResourceWithRawResponse:
    def __init__(self, logpush: LogpushResource) -> None:
        self._logpush = logpush

    @cached_property
    def datasets(self) -> DatasetsResourceWithRawResponse:
        return DatasetsResourceWithRawResponse(self._logpush.datasets)

    @cached_property
    def edge(self) -> EdgeResourceWithRawResponse:
        return EdgeResourceWithRawResponse(self._logpush.edge)

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._logpush.jobs)

    @cached_property
    def ownership(self) -> OwnershipResourceWithRawResponse:
        return OwnershipResourceWithRawResponse(self._logpush.ownership)

    @cached_property
    def validate(self) -> ValidateResourceWithRawResponse:
        return ValidateResourceWithRawResponse(self._logpush.validate)


class AsyncLogpushResourceWithRawResponse:
    def __init__(self, logpush: AsyncLogpushResource) -> None:
        self._logpush = logpush

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithRawResponse:
        return AsyncDatasetsResourceWithRawResponse(self._logpush.datasets)

    @cached_property
    def edge(self) -> AsyncEdgeResourceWithRawResponse:
        return AsyncEdgeResourceWithRawResponse(self._logpush.edge)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._logpush.jobs)

    @cached_property
    def ownership(self) -> AsyncOwnershipResourceWithRawResponse:
        return AsyncOwnershipResourceWithRawResponse(self._logpush.ownership)

    @cached_property
    def validate(self) -> AsyncValidateResourceWithRawResponse:
        return AsyncValidateResourceWithRawResponse(self._logpush.validate)


class LogpushResourceWithStreamingResponse:
    def __init__(self, logpush: LogpushResource) -> None:
        self._logpush = logpush

    @cached_property
    def datasets(self) -> DatasetsResourceWithStreamingResponse:
        return DatasetsResourceWithStreamingResponse(self._logpush.datasets)

    @cached_property
    def edge(self) -> EdgeResourceWithStreamingResponse:
        return EdgeResourceWithStreamingResponse(self._logpush.edge)

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._logpush.jobs)

    @cached_property
    def ownership(self) -> OwnershipResourceWithStreamingResponse:
        return OwnershipResourceWithStreamingResponse(self._logpush.ownership)

    @cached_property
    def validate(self) -> ValidateResourceWithStreamingResponse:
        return ValidateResourceWithStreamingResponse(self._logpush.validate)


class AsyncLogpushResourceWithStreamingResponse:
    def __init__(self, logpush: AsyncLogpushResource) -> None:
        self._logpush = logpush

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithStreamingResponse:
        return AsyncDatasetsResourceWithStreamingResponse(self._logpush.datasets)

    @cached_property
    def edge(self) -> AsyncEdgeResourceWithStreamingResponse:
        return AsyncEdgeResourceWithStreamingResponse(self._logpush.edge)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._logpush.jobs)

    @cached_property
    def ownership(self) -> AsyncOwnershipResourceWithStreamingResponse:
        return AsyncOwnershipResourceWithStreamingResponse(self._logpush.ownership)

    @cached_property
    def validate(self) -> AsyncValidateResourceWithStreamingResponse:
        return AsyncValidateResourceWithStreamingResponse(self._logpush.validate)
