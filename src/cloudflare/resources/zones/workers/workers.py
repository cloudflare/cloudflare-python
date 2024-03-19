# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .script import (
    Script,
    AsyncScript,
    ScriptWithRawResponse,
    AsyncScriptWithRawResponse,
    ScriptWithStreamingResponse,
    AsyncScriptWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Workers", "AsyncWorkers"]


class Workers(SyncAPIResource):
    @cached_property
    def script(self) -> Script:
        return Script(self._client)

    @cached_property
    def with_raw_response(self) -> WorkersWithRawResponse:
        return WorkersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkersWithStreamingResponse:
        return WorkersWithStreamingResponse(self)


class AsyncWorkers(AsyncAPIResource):
    @cached_property
    def script(self) -> AsyncScript:
        return AsyncScript(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWorkersWithRawResponse:
        return AsyncWorkersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkersWithStreamingResponse:
        return AsyncWorkersWithStreamingResponse(self)


class WorkersWithRawResponse:
    def __init__(self, workers: Workers) -> None:
        self._workers = workers

    @cached_property
    def script(self) -> ScriptWithRawResponse:
        return ScriptWithRawResponse(self._workers.script)


class AsyncWorkersWithRawResponse:
    def __init__(self, workers: AsyncWorkers) -> None:
        self._workers = workers

    @cached_property
    def script(self) -> AsyncScriptWithRawResponse:
        return AsyncScriptWithRawResponse(self._workers.script)


class WorkersWithStreamingResponse:
    def __init__(self, workers: Workers) -> None:
        self._workers = workers

    @cached_property
    def script(self) -> ScriptWithStreamingResponse:
        return ScriptWithStreamingResponse(self._workers.script)


class AsyncWorkersWithStreamingResponse:
    def __init__(self, workers: AsyncWorkers) -> None:
        self._workers = workers

    @cached_property
    def script(self) -> AsyncScriptWithStreamingResponse:
        return AsyncScriptWithStreamingResponse(self._workers.script)
