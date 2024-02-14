# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .content import Content, AsyncContent

from ..._compat import cached_property

from .content_v2 import ContentV2, AsyncContentV2

from .settings import Settings, AsyncSettings

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from .content import (
    Content,
    AsyncContent,
    ContentWithRawResponse,
    AsyncContentWithRawResponse,
    ContentWithStreamingResponse,
    AsyncContentWithStreamingResponse,
)
from .content_v2 import (
    ContentV2,
    AsyncContentV2,
    ContentV2WithRawResponse,
    AsyncContentV2WithRawResponse,
    ContentV2WithStreamingResponse,
    AsyncContentV2WithStreamingResponse,
)
from .settings import (
    Settings,
    AsyncSettings,
    SettingsWithRawResponse,
    AsyncSettingsWithRawResponse,
    SettingsWithStreamingResponse,
    AsyncSettingsWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["WorkerScripts", "AsyncWorkerScripts"]


class WorkerScripts(SyncAPIResource):
    @cached_property
    def content(self) -> Content:
        return Content(self._client)

    @cached_property
    def content_v2(self) -> ContentV2:
        return ContentV2(self._client)

    @cached_property
    def settings(self) -> Settings:
        return Settings(self._client)

    @cached_property
    def with_raw_response(self) -> WorkerScriptsWithRawResponse:
        return WorkerScriptsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkerScriptsWithStreamingResponse:
        return WorkerScriptsWithStreamingResponse(self)


class AsyncWorkerScripts(AsyncAPIResource):
    @cached_property
    def content(self) -> AsyncContent:
        return AsyncContent(self._client)

    @cached_property
    def content_v2(self) -> AsyncContentV2:
        return AsyncContentV2(self._client)

    @cached_property
    def settings(self) -> AsyncSettings:
        return AsyncSettings(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWorkerScriptsWithRawResponse:
        return AsyncWorkerScriptsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkerScriptsWithStreamingResponse:
        return AsyncWorkerScriptsWithStreamingResponse(self)


class WorkerScriptsWithRawResponse:
    def __init__(self, worker_scripts: WorkerScripts) -> None:
        self._worker_scripts = worker_scripts

    @cached_property
    def content(self) -> ContentWithRawResponse:
        return ContentWithRawResponse(self._worker_scripts.content)

    @cached_property
    def content_v2(self) -> ContentV2WithRawResponse:
        return ContentV2WithRawResponse(self._worker_scripts.content_v2)

    @cached_property
    def settings(self) -> SettingsWithRawResponse:
        return SettingsWithRawResponse(self._worker_scripts.settings)


class AsyncWorkerScriptsWithRawResponse:
    def __init__(self, worker_scripts: AsyncWorkerScripts) -> None:
        self._worker_scripts = worker_scripts

    @cached_property
    def content(self) -> AsyncContentWithRawResponse:
        return AsyncContentWithRawResponse(self._worker_scripts.content)

    @cached_property
    def content_v2(self) -> AsyncContentV2WithRawResponse:
        return AsyncContentV2WithRawResponse(self._worker_scripts.content_v2)

    @cached_property
    def settings(self) -> AsyncSettingsWithRawResponse:
        return AsyncSettingsWithRawResponse(self._worker_scripts.settings)


class WorkerScriptsWithStreamingResponse:
    def __init__(self, worker_scripts: WorkerScripts) -> None:
        self._worker_scripts = worker_scripts

    @cached_property
    def content(self) -> ContentWithStreamingResponse:
        return ContentWithStreamingResponse(self._worker_scripts.content)

    @cached_property
    def content_v2(self) -> ContentV2WithStreamingResponse:
        return ContentV2WithStreamingResponse(self._worker_scripts.content_v2)

    @cached_property
    def settings(self) -> SettingsWithStreamingResponse:
        return SettingsWithStreamingResponse(self._worker_scripts.settings)


class AsyncWorkerScriptsWithStreamingResponse:
    def __init__(self, worker_scripts: AsyncWorkerScripts) -> None:
        self._worker_scripts = worker_scripts

    @cached_property
    def content(self) -> AsyncContentWithStreamingResponse:
        return AsyncContentWithStreamingResponse(self._worker_scripts.content)

    @cached_property
    def content_v2(self) -> AsyncContentV2WithStreamingResponse:
        return AsyncContentV2WithStreamingResponse(self._worker_scripts.content_v2)

    @cached_property
    def settings(self) -> AsyncSettingsWithStreamingResponse:
        return AsyncSettingsWithStreamingResponse(self._worker_scripts.settings)
