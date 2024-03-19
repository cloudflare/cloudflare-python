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

__all__ = ["KV", "AsyncKV"]


class KV(SyncAPIResource):
    @cached_property
    def namespaces(self) -> Namespaces:
        return Namespaces(self._client)

    @cached_property
    def with_raw_response(self) -> KVWithRawResponse:
        return KVWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KVWithStreamingResponse:
        return KVWithStreamingResponse(self)


class AsyncKV(AsyncAPIResource):
    @cached_property
    def namespaces(self) -> AsyncNamespaces:
        return AsyncNamespaces(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncKVWithRawResponse:
        return AsyncKVWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKVWithStreamingResponse:
        return AsyncKVWithStreamingResponse(self)


class KVWithRawResponse:
    def __init__(self, kv: KV) -> None:
        self._kv = kv

    @cached_property
    def namespaces(self) -> NamespacesWithRawResponse:
        return NamespacesWithRawResponse(self._kv.namespaces)


class AsyncKVWithRawResponse:
    def __init__(self, kv: AsyncKV) -> None:
        self._kv = kv

    @cached_property
    def namespaces(self) -> AsyncNamespacesWithRawResponse:
        return AsyncNamespacesWithRawResponse(self._kv.namespaces)


class KVWithStreamingResponse:
    def __init__(self, kv: KV) -> None:
        self._kv = kv

    @cached_property
    def namespaces(self) -> NamespacesWithStreamingResponse:
        return NamespacesWithStreamingResponse(self._kv.namespaces)


class AsyncKVWithStreamingResponse:
    def __init__(self, kv: AsyncKV) -> None:
        self._kv = kv

    @cached_property
    def namespaces(self) -> AsyncNamespacesWithStreamingResponse:
        return AsyncNamespacesWithStreamingResponse(self._kv.namespaces)
