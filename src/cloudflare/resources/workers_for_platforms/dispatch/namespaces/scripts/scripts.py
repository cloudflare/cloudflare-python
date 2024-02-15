# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .content import (
    Content,
    AsyncContent,
    ContentWithRawResponse,
    AsyncContentWithRawResponse,
    ContentWithStreamingResponse,
    AsyncContentWithStreamingResponse,
)
from .settings import (
    Settings,
    AsyncSettings,
    SettingsWithRawResponse,
    AsyncSettingsWithRawResponse,
    SettingsWithStreamingResponse,
    AsyncSettingsWithStreamingResponse,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Scripts", "AsyncScripts"]


class Scripts(SyncAPIResource):
    @cached_property
    def content(self) -> Content:
        return Content(self._client)

    @cached_property
    def settings(self) -> Settings:
        return Settings(self._client)

    @cached_property
    def with_raw_response(self) -> ScriptsWithRawResponse:
        return ScriptsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScriptsWithStreamingResponse:
        return ScriptsWithStreamingResponse(self)


class AsyncScripts(AsyncAPIResource):
    @cached_property
    def content(self) -> AsyncContent:
        return AsyncContent(self._client)

    @cached_property
    def settings(self) -> AsyncSettings:
        return AsyncSettings(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncScriptsWithRawResponse:
        return AsyncScriptsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScriptsWithStreamingResponse:
        return AsyncScriptsWithStreamingResponse(self)


class ScriptsWithRawResponse:
    def __init__(self, scripts: Scripts) -> None:
        self._scripts = scripts

    @cached_property
    def content(self) -> ContentWithRawResponse:
        return ContentWithRawResponse(self._scripts.content)

    @cached_property
    def settings(self) -> SettingsWithRawResponse:
        return SettingsWithRawResponse(self._scripts.settings)


class AsyncScriptsWithRawResponse:
    def __init__(self, scripts: AsyncScripts) -> None:
        self._scripts = scripts

    @cached_property
    def content(self) -> AsyncContentWithRawResponse:
        return AsyncContentWithRawResponse(self._scripts.content)

    @cached_property
    def settings(self) -> AsyncSettingsWithRawResponse:
        return AsyncSettingsWithRawResponse(self._scripts.settings)


class ScriptsWithStreamingResponse:
    def __init__(self, scripts: Scripts) -> None:
        self._scripts = scripts

    @cached_property
    def content(self) -> ContentWithStreamingResponse:
        return ContentWithStreamingResponse(self._scripts.content)

    @cached_property
    def settings(self) -> SettingsWithStreamingResponse:
        return SettingsWithStreamingResponse(self._scripts.settings)


class AsyncScriptsWithStreamingResponse:
    def __init__(self, scripts: AsyncScripts) -> None:
        self._scripts = scripts

    @cached_property
    def content(self) -> AsyncContentWithStreamingResponse:
        return AsyncContentWithStreamingResponse(self._scripts.content)

    @cached_property
    def settings(self) -> AsyncSettingsWithStreamingResponse:
        return AsyncSettingsWithStreamingResponse(self._scripts.settings)
