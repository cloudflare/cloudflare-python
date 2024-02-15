# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .settings.settings import Settings, AsyncSettings

from ..._compat import cached_property

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
from .settings import (
    Settings,
    AsyncSettings,
    SettingsWithRawResponse,
    AsyncSettingsWithRawResponse,
    SettingsWithStreamingResponse,
    AsyncSettingsWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["Hostnames", "AsyncHostnames"]


class Hostnames(SyncAPIResource):
    @cached_property
    def settings(self) -> Settings:
        return Settings(self._client)

    @cached_property
    def with_raw_response(self) -> HostnamesWithRawResponse:
        return HostnamesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HostnamesWithStreamingResponse:
        return HostnamesWithStreamingResponse(self)


class AsyncHostnames(AsyncAPIResource):
    @cached_property
    def settings(self) -> AsyncSettings:
        return AsyncSettings(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHostnamesWithRawResponse:
        return AsyncHostnamesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHostnamesWithStreamingResponse:
        return AsyncHostnamesWithStreamingResponse(self)


class HostnamesWithRawResponse:
    def __init__(self, hostnames: Hostnames) -> None:
        self._hostnames = hostnames

    @cached_property
    def settings(self) -> SettingsWithRawResponse:
        return SettingsWithRawResponse(self._hostnames.settings)


class AsyncHostnamesWithRawResponse:
    def __init__(self, hostnames: AsyncHostnames) -> None:
        self._hostnames = hostnames

    @cached_property
    def settings(self) -> AsyncSettingsWithRawResponse:
        return AsyncSettingsWithRawResponse(self._hostnames.settings)


class HostnamesWithStreamingResponse:
    def __init__(self, hostnames: Hostnames) -> None:
        self._hostnames = hostnames

    @cached_property
    def settings(self) -> SettingsWithStreamingResponse:
        return SettingsWithStreamingResponse(self._hostnames.settings)


class AsyncHostnamesWithStreamingResponse:
    def __init__(self, hostnames: AsyncHostnames) -> None:
        self._hostnames = hostnames

    @cached_property
    def settings(self) -> AsyncSettingsWithStreamingResponse:
        return AsyncSettingsWithStreamingResponse(self._hostnames.settings)
