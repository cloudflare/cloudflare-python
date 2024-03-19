# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .requests import (
    Requests,
    AsyncRequests,
    RequestsWithRawResponse,
    AsyncRequestsWithRawResponse,
    RequestsWithStreamingResponse,
    AsyncRequestsWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .requests.requests import Requests, AsyncRequests

__all__ = ["CloudforceOne", "AsyncCloudforceOne"]


class CloudforceOne(SyncAPIResource):
    @cached_property
    def requests(self) -> Requests:
        return Requests(self._client)

    @cached_property
    def with_raw_response(self) -> CloudforceOneWithRawResponse:
        return CloudforceOneWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CloudforceOneWithStreamingResponse:
        return CloudforceOneWithStreamingResponse(self)


class AsyncCloudforceOne(AsyncAPIResource):
    @cached_property
    def requests(self) -> AsyncRequests:
        return AsyncRequests(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCloudforceOneWithRawResponse:
        return AsyncCloudforceOneWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCloudforceOneWithStreamingResponse:
        return AsyncCloudforceOneWithStreamingResponse(self)


class CloudforceOneWithRawResponse:
    def __init__(self, cloudforce_one: CloudforceOne) -> None:
        self._cloudforce_one = cloudforce_one

    @cached_property
    def requests(self) -> RequestsWithRawResponse:
        return RequestsWithRawResponse(self._cloudforce_one.requests)


class AsyncCloudforceOneWithRawResponse:
    def __init__(self, cloudforce_one: AsyncCloudforceOne) -> None:
        self._cloudforce_one = cloudforce_one

    @cached_property
    def requests(self) -> AsyncRequestsWithRawResponse:
        return AsyncRequestsWithRawResponse(self._cloudforce_one.requests)


class CloudforceOneWithStreamingResponse:
    def __init__(self, cloudforce_one: CloudforceOne) -> None:
        self._cloudforce_one = cloudforce_one

    @cached_property
    def requests(self) -> RequestsWithStreamingResponse:
        return RequestsWithStreamingResponse(self._cloudforce_one.requests)


class AsyncCloudforceOneWithStreamingResponse:
    def __init__(self, cloudforce_one: AsyncCloudforceOne) -> None:
        self._cloudforce_one = cloudforce_one

    @cached_property
    def requests(self) -> AsyncRequestsWithStreamingResponse:
        return AsyncRequestsWithStreamingResponse(self._cloudforce_one.requests)
