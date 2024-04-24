# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .requests import (
    RequestsResource,
    AsyncRequestsResource,
    RequestsResourceWithRawResponse,
    AsyncRequestsResourceWithRawResponse,
    RequestsResourceWithStreamingResponse,
    AsyncRequestsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .requests.requests import RequestsResource, AsyncRequestsResource

__all__ = ["CloudforceOneResource", "AsyncCloudforceOneResource"]


class CloudforceOneResource(SyncAPIResource):
    @cached_property
    def requests(self) -> RequestsResource:
        return RequestsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CloudforceOneResourceWithRawResponse:
        return CloudforceOneResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CloudforceOneResourceWithStreamingResponse:
        return CloudforceOneResourceWithStreamingResponse(self)


class AsyncCloudforceOneResource(AsyncAPIResource):
    @cached_property
    def requests(self) -> AsyncRequestsResource:
        return AsyncRequestsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCloudforceOneResourceWithRawResponse:
        return AsyncCloudforceOneResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCloudforceOneResourceWithStreamingResponse:
        return AsyncCloudforceOneResourceWithStreamingResponse(self)


class CloudforceOneResourceWithRawResponse:
    def __init__(self, cloudforce_one: CloudforceOneResource) -> None:
        self._cloudforce_one = cloudforce_one

    @cached_property
    def requests(self) -> RequestsResourceWithRawResponse:
        return RequestsResourceWithRawResponse(self._cloudforce_one.requests)


class AsyncCloudforceOneResourceWithRawResponse:
    def __init__(self, cloudforce_one: AsyncCloudforceOneResource) -> None:
        self._cloudforce_one = cloudforce_one

    @cached_property
    def requests(self) -> AsyncRequestsResourceWithRawResponse:
        return AsyncRequestsResourceWithRawResponse(self._cloudforce_one.requests)


class CloudforceOneResourceWithStreamingResponse:
    def __init__(self, cloudforce_one: CloudforceOneResource) -> None:
        self._cloudforce_one = cloudforce_one

    @cached_property
    def requests(self) -> RequestsResourceWithStreamingResponse:
        return RequestsResourceWithStreamingResponse(self._cloudforce_one.requests)


class AsyncCloudforceOneResourceWithStreamingResponse:
    def __init__(self, cloudforce_one: AsyncCloudforceOneResource) -> None:
        self._cloudforce_one = cloudforce_one

    @cached_property
    def requests(self) -> AsyncRequestsResourceWithStreamingResponse:
        return AsyncRequestsResourceWithStreamingResponse(self._cloudforce_one.requests)
