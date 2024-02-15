# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ...._compat import cached_property
from .namespaces import (
    Namespaces,
    AsyncNamespaces,
    NamespacesWithRawResponse,
    AsyncNamespacesWithRawResponse,
    NamespacesWithStreamingResponse,
    AsyncNamespacesWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from .namespaces.namespaces import Namespaces, AsyncNamespaces

__all__ = ["Kv", "AsyncKv"]


class Kv(SyncAPIResource):
    @cached_property
    def namespaces(self) -> Namespaces:
        return Namespaces(self._client)

    @cached_property
    def with_raw_response(self) -> KvWithRawResponse:
        return KvWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KvWithStreamingResponse:
        return KvWithStreamingResponse(self)


class AsyncKv(AsyncAPIResource):
    @cached_property
    def namespaces(self) -> AsyncNamespaces:
        return AsyncNamespaces(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncKvWithRawResponse:
        return AsyncKvWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKvWithStreamingResponse:
        return AsyncKvWithStreamingResponse(self)


class KvWithRawResponse:
    def __init__(self, kv: Kv) -> None:
        self._kv = kv

    @cached_property
    def namespaces(self) -> NamespacesWithRawResponse:
        return NamespacesWithRawResponse(self._kv.namespaces)


class AsyncKvWithRawResponse:
    def __init__(self, kv: AsyncKv) -> None:
        self._kv = kv

    @cached_property
    def namespaces(self) -> AsyncNamespacesWithRawResponse:
        return AsyncNamespacesWithRawResponse(self._kv.namespaces)


class KvWithStreamingResponse:
    def __init__(self, kv: Kv) -> None:
        self._kv = kv

    @cached_property
    def namespaces(self) -> NamespacesWithStreamingResponse:
        return NamespacesWithStreamingResponse(self._kv.namespaces)


class AsyncKvWithStreamingResponse:
    def __init__(self, kv: AsyncKv) -> None:
        self._kv = kv

    @cached_property
    def namespaces(self) -> AsyncNamespacesWithStreamingResponse:
        return AsyncNamespacesWithStreamingResponse(self._kv.namespaces)
