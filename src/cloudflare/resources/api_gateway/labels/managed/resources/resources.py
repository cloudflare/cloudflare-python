# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .operation import (
    OperationResource,
    AsyncOperationResource,
    OperationResourceWithRawResponse,
    AsyncOperationResourceWithRawResponse,
    OperationResourceWithStreamingResponse,
    AsyncOperationResourceWithStreamingResponse,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ResourcesResource", "AsyncResourcesResource"]


class ResourcesResource(SyncAPIResource):
    @cached_property
    def operation(self) -> OperationResource:
        return OperationResource(self._client)

    @cached_property
    def with_raw_response(self) -> ResourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ResourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ResourcesResourceWithStreamingResponse(self)


class AsyncResourcesResource(AsyncAPIResource):
    @cached_property
    def operation(self) -> AsyncOperationResource:
        return AsyncOperationResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncResourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncResourcesResourceWithStreamingResponse(self)


class ResourcesResourceWithRawResponse:
    def __init__(self, resources: ResourcesResource) -> None:
        self._resources = resources

    @cached_property
    def operation(self) -> OperationResourceWithRawResponse:
        return OperationResourceWithRawResponse(self._resources.operation)


class AsyncResourcesResourceWithRawResponse:
    def __init__(self, resources: AsyncResourcesResource) -> None:
        self._resources = resources

    @cached_property
    def operation(self) -> AsyncOperationResourceWithRawResponse:
        return AsyncOperationResourceWithRawResponse(self._resources.operation)


class ResourcesResourceWithStreamingResponse:
    def __init__(self, resources: ResourcesResource) -> None:
        self._resources = resources

    @cached_property
    def operation(self) -> OperationResourceWithStreamingResponse:
        return OperationResourceWithStreamingResponse(self._resources.operation)


class AsyncResourcesResourceWithStreamingResponse:
    def __init__(self, resources: AsyncResourcesResource) -> None:
        self._resources = resources

    @cached_property
    def operation(self) -> AsyncOperationResourceWithStreamingResponse:
        return AsyncOperationResourceWithStreamingResponse(self._resources.operation)
