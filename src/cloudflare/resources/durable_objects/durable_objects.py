# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .namespaces.namespaces import (
    NamespacesResource,
    AsyncNamespacesResource,
    NamespacesResourceWithRawResponse,
    AsyncNamespacesResourceWithRawResponse,
    NamespacesResourceWithStreamingResponse,
    AsyncNamespacesResourceWithStreamingResponse,
)

__all__ = ["DurableObjectsResource", "AsyncDurableObjectsResource"]


class DurableObjectsResource(SyncAPIResource):
    @cached_property
    def namespaces(self) -> NamespacesResource:
        return NamespacesResource(self._client)

    @cached_property
    def with_raw_response(self) -> DurableObjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DurableObjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DurableObjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DurableObjectsResourceWithStreamingResponse(self)


class AsyncDurableObjectsResource(AsyncAPIResource):
    @cached_property
    def namespaces(self) -> AsyncNamespacesResource:
        return AsyncNamespacesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDurableObjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDurableObjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDurableObjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDurableObjectsResourceWithStreamingResponse(self)


class DurableObjectsResourceWithRawResponse:
    def __init__(self, durable_objects: DurableObjectsResource) -> None:
        self._durable_objects = durable_objects

    @cached_property
    def namespaces(self) -> NamespacesResourceWithRawResponse:
        return NamespacesResourceWithRawResponse(self._durable_objects.namespaces)


class AsyncDurableObjectsResourceWithRawResponse:
    def __init__(self, durable_objects: AsyncDurableObjectsResource) -> None:
        self._durable_objects = durable_objects

    @cached_property
    def namespaces(self) -> AsyncNamespacesResourceWithRawResponse:
        return AsyncNamespacesResourceWithRawResponse(self._durable_objects.namespaces)


class DurableObjectsResourceWithStreamingResponse:
    def __init__(self, durable_objects: DurableObjectsResource) -> None:
        self._durable_objects = durable_objects

    @cached_property
    def namespaces(self) -> NamespacesResourceWithStreamingResponse:
        return NamespacesResourceWithStreamingResponse(self._durable_objects.namespaces)


class AsyncDurableObjectsResourceWithStreamingResponse:
    def __init__(self, durable_objects: AsyncDurableObjectsResource) -> None:
        self._durable_objects = durable_objects

    @cached_property
    def namespaces(self) -> AsyncNamespacesResourceWithStreamingResponse:
        return AsyncNamespacesResourceWithStreamingResponse(self._durable_objects.namespaces)
