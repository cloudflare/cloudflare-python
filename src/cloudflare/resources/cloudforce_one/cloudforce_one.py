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
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CloudforceOneResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CloudforceOneResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CloudforceOneResourceWithStreamingResponse(self)


class AsyncCloudforceOneResource(AsyncAPIResource):
    @cached_property
    def requests(self) -> AsyncRequestsResource:
        return AsyncRequestsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCloudforceOneResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCloudforceOneResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCloudforceOneResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
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
