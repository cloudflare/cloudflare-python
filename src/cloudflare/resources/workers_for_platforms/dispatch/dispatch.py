# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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

__all__ = ["Dispatch", "AsyncDispatch"]


class Dispatch(SyncAPIResource):
    @cached_property
    def namespaces(self) -> Namespaces:
        return Namespaces(self._client)

    @cached_property
    def with_raw_response(self) -> DispatchWithRawResponse:
        return DispatchWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DispatchWithStreamingResponse:
        return DispatchWithStreamingResponse(self)


class AsyncDispatch(AsyncAPIResource):
    @cached_property
    def namespaces(self) -> AsyncNamespaces:
        return AsyncNamespaces(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDispatchWithRawResponse:
        return AsyncDispatchWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDispatchWithStreamingResponse:
        return AsyncDispatchWithStreamingResponse(self)


class DispatchWithRawResponse:
    def __init__(self, dispatch: Dispatch) -> None:
        self._dispatch = dispatch

    @cached_property
    def namespaces(self) -> NamespacesWithRawResponse:
        return NamespacesWithRawResponse(self._dispatch.namespaces)


class AsyncDispatchWithRawResponse:
    def __init__(self, dispatch: AsyncDispatch) -> None:
        self._dispatch = dispatch

    @cached_property
    def namespaces(self) -> AsyncNamespacesWithRawResponse:
        return AsyncNamespacesWithRawResponse(self._dispatch.namespaces)


class DispatchWithStreamingResponse:
    def __init__(self, dispatch: Dispatch) -> None:
        self._dispatch = dispatch

    @cached_property
    def namespaces(self) -> NamespacesWithStreamingResponse:
        return NamespacesWithStreamingResponse(self._dispatch.namespaces)


class AsyncDispatchWithStreamingResponse:
    def __init__(self, dispatch: AsyncDispatch) -> None:
        self._dispatch = dispatch

    @cached_property
    def namespaces(self) -> AsyncNamespacesWithStreamingResponse:
        return AsyncNamespacesWithStreamingResponse(self._dispatch.namespaces)
