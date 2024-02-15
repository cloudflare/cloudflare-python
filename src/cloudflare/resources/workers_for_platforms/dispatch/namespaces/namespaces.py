# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .scripts import (
    Scripts,
    AsyncScripts,
    ScriptsWithRawResponse,
    AsyncScriptsWithRawResponse,
    ScriptsWithStreamingResponse,
    AsyncScriptsWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .scripts.scripts import Scripts, AsyncScripts

__all__ = ["Namespaces", "AsyncNamespaces"]


class Namespaces(SyncAPIResource):
    @cached_property
    def scripts(self) -> Scripts:
        return Scripts(self._client)

    @cached_property
    def with_raw_response(self) -> NamespacesWithRawResponse:
        return NamespacesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NamespacesWithStreamingResponse:
        return NamespacesWithStreamingResponse(self)


class AsyncNamespaces(AsyncAPIResource):
    @cached_property
    def scripts(self) -> AsyncScripts:
        return AsyncScripts(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNamespacesWithRawResponse:
        return AsyncNamespacesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNamespacesWithStreamingResponse:
        return AsyncNamespacesWithStreamingResponse(self)


class NamespacesWithRawResponse:
    def __init__(self, namespaces: Namespaces) -> None:
        self._namespaces = namespaces

    @cached_property
    def scripts(self) -> ScriptsWithRawResponse:
        return ScriptsWithRawResponse(self._namespaces.scripts)


class AsyncNamespacesWithRawResponse:
    def __init__(self, namespaces: AsyncNamespaces) -> None:
        self._namespaces = namespaces

    @cached_property
    def scripts(self) -> AsyncScriptsWithRawResponse:
        return AsyncScriptsWithRawResponse(self._namespaces.scripts)


class NamespacesWithStreamingResponse:
    def __init__(self, namespaces: Namespaces) -> None:
        self._namespaces = namespaces

    @cached_property
    def scripts(self) -> ScriptsWithStreamingResponse:
        return ScriptsWithStreamingResponse(self._namespaces.scripts)


class AsyncNamespacesWithStreamingResponse:
    def __init__(self, namespaces: AsyncNamespaces) -> None:
        self._namespaces = namespaces

    @cached_property
    def scripts(self) -> AsyncScriptsWithStreamingResponse:
        return AsyncScriptsWithStreamingResponse(self._namespaces.scripts)
