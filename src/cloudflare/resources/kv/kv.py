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

__all__ = ["KVResource", "AsyncKVResource"]


class KVResource(SyncAPIResource):
    @cached_property
    def namespaces(self) -> NamespacesResource:
        return NamespacesResource(self._client)

    @cached_property
    def with_raw_response(self) -> KVResourceWithRawResponse:
        return KVResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KVResourceWithStreamingResponse:
        return KVResourceWithStreamingResponse(self)


class AsyncKVResource(AsyncAPIResource):
    @cached_property
    def namespaces(self) -> AsyncNamespacesResource:
        return AsyncNamespacesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncKVResourceWithRawResponse:
        return AsyncKVResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKVResourceWithStreamingResponse:
        return AsyncKVResourceWithStreamingResponse(self)


class KVResourceWithRawResponse:
    def __init__(self, kv: KVResource) -> None:
        self._kv = kv

    @cached_property
    def namespaces(self) -> NamespacesResourceWithRawResponse:
        return NamespacesResourceWithRawResponse(self._kv.namespaces)


class AsyncKVResourceWithRawResponse:
    def __init__(self, kv: AsyncKVResource) -> None:
        self._kv = kv

    @cached_property
    def namespaces(self) -> AsyncNamespacesResourceWithRawResponse:
        return AsyncNamespacesResourceWithRawResponse(self._kv.namespaces)


class KVResourceWithStreamingResponse:
    def __init__(self, kv: KVResource) -> None:
        self._kv = kv

    @cached_property
    def namespaces(self) -> NamespacesResourceWithStreamingResponse:
        return NamespacesResourceWithStreamingResponse(self._kv.namespaces)


class AsyncKVResourceWithStreamingResponse:
    def __init__(self, kv: AsyncKVResource) -> None:
        self._kv = kv

    @cached_property
    def namespaces(self) -> AsyncNamespacesResourceWithStreamingResponse:
        return AsyncNamespacesResourceWithStreamingResponse(self._kv.namespaces)
