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
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource

__all__ = ["RemediationsResource", "AsyncRemediationsResource"]


class RemediationsResource(SyncAPIResource):
    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RemediationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RemediationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RemediationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RemediationsResourceWithStreamingResponse(self)


class AsyncRemediationsResource(AsyncAPIResource):
    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRemediationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRemediationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRemediationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRemediationsResourceWithStreamingResponse(self)


class RemediationsResourceWithRawResponse:
    def __init__(self, remediations: RemediationsResource) -> None:
        self._remediations = remediations

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._remediations.jobs)


class AsyncRemediationsResourceWithRawResponse:
    def __init__(self, remediations: AsyncRemediationsResource) -> None:
        self._remediations = remediations

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._remediations.jobs)


class RemediationsResourceWithStreamingResponse:
    def __init__(self, remediations: RemediationsResource) -> None:
        self._remediations = remediations

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._remediations.jobs)


class AsyncRemediationsResourceWithStreamingResponse:
    def __init__(self, remediations: AsyncRemediationsResource) -> None:
        self._remediations = remediations

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._remediations.jobs)
