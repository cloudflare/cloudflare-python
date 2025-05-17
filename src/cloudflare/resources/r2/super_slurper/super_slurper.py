# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .jobs.jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .connectivity_precheck import (
    ConnectivityPrecheckResource,
    AsyncConnectivityPrecheckResource,
    ConnectivityPrecheckResourceWithRawResponse,
    AsyncConnectivityPrecheckResourceWithRawResponse,
    ConnectivityPrecheckResourceWithStreamingResponse,
    AsyncConnectivityPrecheckResourceWithStreamingResponse,
)

__all__ = ["SuperSlurperResource", "AsyncSuperSlurperResource"]


class SuperSlurperResource(SyncAPIResource):
    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def connectivity_precheck(self) -> ConnectivityPrecheckResource:
        return ConnectivityPrecheckResource(self._client)

    @cached_property
    def with_raw_response(self) -> SuperSlurperResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SuperSlurperResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SuperSlurperResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SuperSlurperResourceWithStreamingResponse(self)


class AsyncSuperSlurperResource(AsyncAPIResource):
    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def connectivity_precheck(self) -> AsyncConnectivityPrecheckResource:
        return AsyncConnectivityPrecheckResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSuperSlurperResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSuperSlurperResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSuperSlurperResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSuperSlurperResourceWithStreamingResponse(self)


class SuperSlurperResourceWithRawResponse:
    def __init__(self, super_slurper: SuperSlurperResource) -> None:
        self._super_slurper = super_slurper

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._super_slurper.jobs)

    @cached_property
    def connectivity_precheck(self) -> ConnectivityPrecheckResourceWithRawResponse:
        return ConnectivityPrecheckResourceWithRawResponse(self._super_slurper.connectivity_precheck)


class AsyncSuperSlurperResourceWithRawResponse:
    def __init__(self, super_slurper: AsyncSuperSlurperResource) -> None:
        self._super_slurper = super_slurper

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._super_slurper.jobs)

    @cached_property
    def connectivity_precheck(self) -> AsyncConnectivityPrecheckResourceWithRawResponse:
        return AsyncConnectivityPrecheckResourceWithRawResponse(self._super_slurper.connectivity_precheck)


class SuperSlurperResourceWithStreamingResponse:
    def __init__(self, super_slurper: SuperSlurperResource) -> None:
        self._super_slurper = super_slurper

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._super_slurper.jobs)

    @cached_property
    def connectivity_precheck(self) -> ConnectivityPrecheckResourceWithStreamingResponse:
        return ConnectivityPrecheckResourceWithStreamingResponse(self._super_slurper.connectivity_precheck)


class AsyncSuperSlurperResourceWithStreamingResponse:
    def __init__(self, super_slurper: AsyncSuperSlurperResource) -> None:
        self._super_slurper = super_slurper

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._super_slurper.jobs)

    @cached_property
    def connectivity_precheck(self) -> AsyncConnectivityPrecheckResourceWithStreamingResponse:
        return AsyncConnectivityPrecheckResourceWithStreamingResponse(self._super_slurper.connectivity_precheck)
