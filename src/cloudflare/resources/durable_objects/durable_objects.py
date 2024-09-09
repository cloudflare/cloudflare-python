# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .namespaces import (
    NamespacesResource,
    AsyncNamespacesResource,
    NamespacesResourceWithRawResponse,
    AsyncNamespacesResourceWithRawResponse,
    NamespacesResourceWithStreamingResponse,
    AsyncNamespacesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .namespaces.namespaces import NamespacesResource, AsyncNamespacesResource

__all__ = ["DurableObjectsResource", "AsyncDurableObjectsResource"]


class DurableObjectsResource(SyncAPIResource):
    @cached_property
    def namespaces(self) -> NamespacesResource:
        return NamespacesResource(self._client)

    @cached_property
    def with_raw_response(self) -> DurableObjectsResourceWithRawResponse:
        return DurableObjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DurableObjectsResourceWithStreamingResponse:
        return DurableObjectsResourceWithStreamingResponse(self)


class AsyncDurableObjectsResource(AsyncAPIResource):
    @cached_property
    def namespaces(self) -> AsyncNamespacesResource:
        return AsyncNamespacesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDurableObjectsResourceWithRawResponse:
        return AsyncDurableObjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDurableObjectsResourceWithStreamingResponse:
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
