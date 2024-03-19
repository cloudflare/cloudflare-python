# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .namespaces import (
    Namespaces,
    AsyncNamespaces,
    NamespacesWithRawResponse,
    AsyncNamespacesWithRawResponse,
    NamespacesWithStreamingResponse,
    AsyncNamespacesWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .namespaces.namespaces import Namespaces, AsyncNamespaces

__all__ = ["DurableObjects", "AsyncDurableObjects"]


class DurableObjects(SyncAPIResource):
    @cached_property
    def namespaces(self) -> Namespaces:
        return Namespaces(self._client)

    @cached_property
    def with_raw_response(self) -> DurableObjectsWithRawResponse:
        return DurableObjectsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DurableObjectsWithStreamingResponse:
        return DurableObjectsWithStreamingResponse(self)


class AsyncDurableObjects(AsyncAPIResource):
    @cached_property
    def namespaces(self) -> AsyncNamespaces:
        return AsyncNamespaces(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDurableObjectsWithRawResponse:
        return AsyncDurableObjectsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDurableObjectsWithStreamingResponse:
        return AsyncDurableObjectsWithStreamingResponse(self)


class DurableObjectsWithRawResponse:
    def __init__(self, durable_objects: DurableObjects) -> None:
        self._durable_objects = durable_objects

    @cached_property
    def namespaces(self) -> NamespacesWithRawResponse:
        return NamespacesWithRawResponse(self._durable_objects.namespaces)


class AsyncDurableObjectsWithRawResponse:
    def __init__(self, durable_objects: AsyncDurableObjects) -> None:
        self._durable_objects = durable_objects

    @cached_property
    def namespaces(self) -> AsyncNamespacesWithRawResponse:
        return AsyncNamespacesWithRawResponse(self._durable_objects.namespaces)


class DurableObjectsWithStreamingResponse:
    def __init__(self, durable_objects: DurableObjects) -> None:
        self._durable_objects = durable_objects

    @cached_property
    def namespaces(self) -> NamespacesWithStreamingResponse:
        return NamespacesWithStreamingResponse(self._durable_objects.namespaces)


class AsyncDurableObjectsWithStreamingResponse:
    def __init__(self, durable_objects: AsyncDurableObjects) -> None:
        self._durable_objects = durable_objects

    @cached_property
    def namespaces(self) -> AsyncNamespacesWithStreamingResponse:
        return AsyncNamespacesWithStreamingResponse(self._durable_objects.namespaces)
