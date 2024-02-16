# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .content import Content, AsyncContent

from ....._compat import cached_property

from .settings import Settings, AsyncSettings

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from .....types import shared_params
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
from ....._wrappers import ResultWrapper

__all__ = ["Environments", "AsyncEnvironments"]


class Environments(SyncAPIResource):
    @cached_property
    def content(self) -> Content:
        return Content(self._client)

    @cached_property
    def settings(self) -> Settings:
        return Settings(self._client)

    @cached_property
    def with_raw_response(self) -> EnvironmentsWithRawResponse:
        return EnvironmentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnvironmentsWithStreamingResponse:
        return EnvironmentsWithStreamingResponse(self)


class AsyncEnvironments(AsyncAPIResource):
    @cached_property
    def content(self) -> AsyncContent:
        return AsyncContent(self._client)

    @cached_property
    def settings(self) -> AsyncSettings:
        return AsyncSettings(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEnvironmentsWithRawResponse:
        return AsyncEnvironmentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnvironmentsWithStreamingResponse:
        return AsyncEnvironmentsWithStreamingResponse(self)


class EnvironmentsWithRawResponse:
    def __init__(self, environments: Environments) -> None:
        self._environments = environments

    @cached_property
    def content(self) -> ContentWithRawResponse:
        return ContentWithRawResponse(self._environments.content)

    @cached_property
    def settings(self) -> SettingsWithRawResponse:
        return SettingsWithRawResponse(self._environments.settings)


class AsyncEnvironmentsWithRawResponse:
    def __init__(self, environments: AsyncEnvironments) -> None:
        self._environments = environments

    @cached_property
    def content(self) -> AsyncContentWithRawResponse:
        return AsyncContentWithRawResponse(self._environments.content)

    @cached_property
    def settings(self) -> AsyncSettingsWithRawResponse:
        return AsyncSettingsWithRawResponse(self._environments.settings)


class EnvironmentsWithStreamingResponse:
    def __init__(self, environments: Environments) -> None:
        self._environments = environments

    @cached_property
    def content(self) -> ContentWithStreamingResponse:
        return ContentWithStreamingResponse(self._environments.content)

    @cached_property
    def settings(self) -> SettingsWithStreamingResponse:
        return SettingsWithStreamingResponse(self._environments.settings)


class AsyncEnvironmentsWithStreamingResponse:
    def __init__(self, environments: AsyncEnvironments) -> None:
        self._environments = environments

    @cached_property
    def content(self) -> AsyncContentWithStreamingResponse:
        return AsyncContentWithStreamingResponse(self._environments.content)

    @cached_property
    def settings(self) -> AsyncSettingsWithStreamingResponse:
        return AsyncSettingsWithStreamingResponse(self._environments.settings)
