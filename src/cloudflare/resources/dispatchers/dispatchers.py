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
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Dispatchers", "AsyncDispatchers"]


class Dispatchers(SyncAPIResource):
    @cached_property
    def scripts(self) -> Scripts:
        return Scripts(self._client)

    @cached_property
    def with_raw_response(self) -> DispatchersWithRawResponse:
        return DispatchersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DispatchersWithStreamingResponse:
        return DispatchersWithStreamingResponse(self)


class AsyncDispatchers(AsyncAPIResource):
    @cached_property
    def scripts(self) -> AsyncScripts:
        return AsyncScripts(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDispatchersWithRawResponse:
        return AsyncDispatchersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDispatchersWithStreamingResponse:
        return AsyncDispatchersWithStreamingResponse(self)


class DispatchersWithRawResponse:
    def __init__(self, dispatchers: Dispatchers) -> None:
        self._dispatchers = dispatchers

    @cached_property
    def scripts(self) -> ScriptsWithRawResponse:
        return ScriptsWithRawResponse(self._dispatchers.scripts)


class AsyncDispatchersWithRawResponse:
    def __init__(self, dispatchers: AsyncDispatchers) -> None:
        self._dispatchers = dispatchers

    @cached_property
    def scripts(self) -> AsyncScriptsWithRawResponse:
        return AsyncScriptsWithRawResponse(self._dispatchers.scripts)


class DispatchersWithStreamingResponse:
    def __init__(self, dispatchers: Dispatchers) -> None:
        self._dispatchers = dispatchers

    @cached_property
    def scripts(self) -> ScriptsWithStreamingResponse:
        return ScriptsWithStreamingResponse(self._dispatchers.scripts)


class AsyncDispatchersWithStreamingResponse:
    def __init__(self, dispatchers: AsyncDispatchers) -> None:
        self._dispatchers = dispatchers

    @cached_property
    def scripts(self) -> AsyncScriptsWithStreamingResponse:
        return AsyncScriptsWithStreamingResponse(self._dispatchers.scripts)
